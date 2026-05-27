from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


APP_TITLE = "Temple Culture Explorer"
DATA_DIR = Path("data")


@dataclass(frozen=True)
class Chunk:
    title: str
    source: str
    text: str


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def split_markdown_documents(data_dir: Path) -> list[Chunk]:
    chunks: list[Chunk] = []

    for path in sorted(data_dir.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        sections = re.split(r"(?m)^##\s+", raw)

        for section in sections:
            section = section.strip()
            if not section:
                continue

            lines = section.splitlines()
            title = lines[0].replace("#", "").strip()
            body = clean_text(" ".join(lines[1:]))

            if len(body) < 80:
                continue

            chunks.append(Chunk(title=title, source=path.name, text=body))

    return chunks


def split_text_documents(data_dir: Path) -> list[Chunk]:
    chunks: list[Chunk] = []

    for path in sorted(data_dir.glob("*.txt")):
        raw = path.read_text(encoding="utf-8")
        lines = [line.strip() for line in raw.splitlines() if line.strip()]

        if not lines:
            continue

        title = lines[0]
        body = clean_text(" ".join(lines[1:]))

        if len(body) < 80:
            continue

        chunks.append(Chunk(title=title, source=path.name, text=body))

    return chunks


@st.cache_resource(show_spinner=False)
def build_retriever(data_dir: str) -> tuple[list[Chunk], TfidfVectorizer, object]:
    data_path = Path(data_dir)
    chunks = split_markdown_documents(data_path) + split_text_documents(data_path)

    if not chunks:
        return [], TfidfVectorizer(), None

    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    matrix = vectorizer.fit_transform([f"{chunk.title}. {chunk.text}" for chunk in chunks])
    return chunks, vectorizer, matrix


def retrieve_context(query: str, top_k: int) -> list[tuple[Chunk, float]]:
    chunks, vectorizer, matrix = build_retriever(str(DATA_DIR))

    if not chunks or matrix is None:
        return []

    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix).flatten()
    ranked_indexes = scores.argsort()[::-1][:top_k]

    return [(chunks[index], float(scores[index])) for index in ranked_indexes if scores[index] > 0]


def build_prompt(question: str, matches: list[tuple[Chunk, float]]) -> str:
    context = "\n\n".join(
        f"Source: {chunk.source} | Section: {chunk.title}\n{chunk.text}"
        for chunk, _score in matches
    )

    return (
        "You are a careful temple and culture guide. Answer only from the provided "
        "context. If the context is not enough, say what is missing.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer with practical, culturally respectful detail."
    )


def generate_with_openai(question: str, matches: list[tuple[Chunk, float]]) -> str | None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[{"role": "user", "content": build_prompt(question, matches)}],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as exc:
        return f"OpenAI generation failed, so here is retrieved context instead.\n\nError: {exc}"


def generate_retrieval_answer(question: str, matches: list[tuple[Chunk, float]]) -> str:
    generated = generate_with_openai(question, matches)
    if generated:
        return generated

    if not matches:
        return (
            "I could not find a strong match in the local temple culture notes. "
            "Try asking about architecture, festivals, rituals, travel etiquette, "
            "or a specific temple."
        )

    best_chunk = matches[0][0]
    return (
        f"Based on the local notes, the most relevant section is "
        f"'{best_chunk.title}'.\n\n{best_chunk.text}"
    )


def render_source_card(chunk: Chunk, score: float) -> None:
    with st.expander(f"{chunk.title} - relevance {score:.2f}"):
        st.caption(chunk.source)
        st.write(chunk.text)


def list_knowledge_files(data_dir: Path) -> list[Path]:
    return sorted([*data_dir.glob("*.md"), *data_dir.glob("*.txt")])


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="🛕", layout="wide")

    st.title(APP_TITLE)
    st.caption("A lightweight RAG app for exploring Indian temples, rituals, architecture, and travel etiquette.")

    with st.sidebar:
        st.header("Knowledge Base")
        st.write("Add or edit Markdown and text files in the `data` folder, then refresh the app.")
        if st.button("Reload knowledge base"):
            build_retriever.clear()
            st.rerun()

        knowledge_files = list_knowledge_files(DATA_DIR)
        st.caption(f"{len(knowledge_files)} files loaded from `data/`")
        for file_path in knowledge_files:
            st.write(f"- {file_path.name}")

        top_k = st.slider("Retrieved sources", min_value=1, max_value=5, value=3)
        st.divider()
        st.write("Optional generation")
        st.caption("Set `OPENAI_API_KEY` to generate polished answers from retrieved context.")

    question = st.chat_input("Ask about temples, festivals, rituals, architecture...")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Namaste. Ask me about temple culture, architecture, festivals, etiquette, or heritage sites.",
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if question:
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching the temple culture knowledge base..."):
                matches = retrieve_context(question, top_k)
                answer = generate_retrieval_answer(question, matches)

            st.write(answer)

            if matches:
                st.subheader("Retrieved Sources")
                for chunk, score in matches:
                    render_source_card(chunk, score)

        st.session_state.messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
