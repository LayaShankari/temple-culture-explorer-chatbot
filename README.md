# Temple Explorer RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot designed to help users explore temples, cultural heritage, traditions, festivals, mythology, architecture, and spiritual history across India.

The chatbot retrieves relevant information from temple and cultural datasets and generates intelligent responses using Large Language Models (LLMs).

---

## Features

- Temple information search
- Cultural and historical exploration
- Festival and ritual details
- Temple architecture insights
- Mythology-based Q&A
- Intelligent document retrieval using RAG
- Interactive chatbot interface
- Fast semantic search using vector databases

---

## Project Objectives

The main objective of this project is to build a smart AI assistant that can:

- Answer questions about temples and culture
- Retrieve accurate information from stored datasets
- Provide educational and tourism-related guidance
- Preserve and promote cultural heritage digitally

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask / FastAPI

### AI & RAG
- LangChain
- Sentence Transformers
- OpenAI / Gemini / Ollama
- FAISS / ChromaDB

---

## Project Structure

```plaintext
temple-explorer-rag-chatbot/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── backend/
│   ├── app.py
│   ├── rag_pipeline.py
│   ├── embeddings.py
│   └── requirements.txt
│
├── datasets/
│   ├── temple_history/
│   ├── festivals/
│   ├── mythology/
│   ├── architecture/
│   └── traditions/
│
├── vector_db/
├── embeddings/
├── docs/
├── README.md
└── .gitignore
```

---

## Dataset Sources

The chatbot dataset may include information collected from:

- UNESCO cultural resources
- Government tourism websites
- Temple history articles
- Wikipedia
- Cultural blogs and archives
- Publicly available PDFs and documents

---

## Example User Queries

- “Tell me about Tirupati Temple.”
- “Which temples are famous in South India?”
- “Explain Dravidian temple architecture.”
- “What festivals are celebrated at Meenakshi Temple?”
- “Who built the Brihadeeswara Temple?”

---

## RAG Workflow

1. Collect temple and cultural documents
2. Clean and preprocess data
3. Generate embeddings
4. Store embeddings in vector database
5. Retrieve relevant documents
6. Send retrieved context to LLM
7. Generate intelligent responses

---

## Installation

### Clone Repository

```bash
git clone https://gitlab.com/your-username/temple-explorer-rag-chatbot.git
```

### Move into Project Folder

```bash
cd temple-explorer-rag-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

---

## Future Enhancements

- Voice-enabled chatbot
- Multilingual temple support
- Temple recommendation system
- Interactive maps
- Festival calendar integration
- Mobile application support

---

## Team Members

- Charvi
- Akshaya
- Jyothi
- Laya
- Yavaneetha

---

## License

This project is developed for educational and internship purposes.

---

## Acknowledgement

Special thanks to all open-source communities, cultural resources, and AI technologies that made this project possible.