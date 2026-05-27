# Temple Culture Explorer

A lightweight RAG-based Streamlit application for exploring temple culture, architecture, rituals, festivals, and visitor etiquette.

## Run the app

```powershell
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## How it works

- Markdown and text files in `data/` are split into knowledge chunks.
- A TF-IDF retriever finds the most relevant chunks for each question.
- If `OPENAI_API_KEY` is set, the app generates an answer using the retrieved context.
- If no API key is set, the app still works by returning the best retrieved local answer.

## Add more knowledge

Add more `.md` or `.txt` files inside `data/`. For `.md` files, use `## Section Title` headings. For `.txt` files, put the temple name on the first line and the temple information below it.

Example `.txt` format:

```text
Temple Name, City

History, architecture, rituals, festivals, visitor rules, and cultural notes.
```

Restart or refresh Streamlit after editing the knowledge base.

The app already includes separate `.txt` files for several famous temples and sacred sites, including Tirumala, Kashi Vishwanath, Jagannath Puri, Somnath, Kedarnath, Rameswaram, Kamakhya, Vaishno Devi, Dwarkadhish, Siddhivinayak, Lingaraja, Hampi, Khajuraho, Akshardham Delhi, Mahabodhi Bodh Gaya, and the Golden Temple.

## Optional OpenAI generation

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
streamlit run streamlit_app.py
```
