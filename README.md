# Temple Culture Explorer

Temple Culture Explorer is a Retrieval-Augmented Generation (RAG) chatbot built with Streamlit. It helps users explore famous Indian temples, sacred sites, architecture, rituals, festivals, pilgrimage etiquette, and cultural heritage using a local knowledge base.

The app works even without an API key by retrieving the most relevant local content. If an OpenAI API key is available, it can generate a more polished answer using the retrieved context.

## Features

- Streamlit chatbot interface
- Local RAG-style retrieval from temple knowledge files
- Supports `.md` and `.txt` files inside the `data/` folder
- Separate text files for famous temples and sacred sites in India
- Sidebar list of loaded knowledge files
- Reload button to refresh the knowledge base after adding new files
- Optional OpenAI-powered answer generation
- Works in fallback mode without an LLM API key

## Tech Stack

- Python
- Streamlit
- scikit-learn
- TF-IDF vectorization
- Cosine similarity retrieval
- Optional OpenAI API integration

## Project Structure

```text
global-cultural-explorer-rag-chatbot/
├── data/
│   ├── akshardham_delhi.txt
│   ├── brihadeeswara_temple.txt
│   ├── dwarkadhish_temple.txt
│   ├── jagannath_temple_puri.txt
│   ├── kashi_vishwanath_temple.txt
│   ├── kedarnath_temple.txt
│   ├── meenakshi_amman_temple.txt
│   ├── temple_culture_notes.md
│   └── ...
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Included Knowledge Base

The app includes information about several famous temples and sacred sites, including:

- Kashi Vishwanath Temple, Varanasi
- Sri Venkateswara Temple, Tirumala
- Jagannath Temple, Puri
- Somnath Temple, Gujarat
- Kedarnath Temple, Uttarakhand
- Ramanathaswamy Temple, Rameswaram
- Meenakshi Amman Temple, Madurai
- Brihadeeswara Temple, Thanjavur
- Konark Sun Temple, Odisha
- Kamakhya Temple, Guwahati
- Vaishno Devi Temple, Katra
- Dwarkadhish Temple, Dwarka
- Siddhivinayak Temple, Mumbai
- Lingaraja Temple, Bhubaneswar
- Virupaksha Temple, Hampi
- Kandariya Mahadeva Temple, Khajuraho
- Swaminarayan Akshardham, Delhi
- Mahabodhi Temple, Bodh Gaya
- Golden Temple, Amritsar

## Installation

Clone the repository:

```bash
git clone https://code.swecha.org/Charvi_Gandla/global-cultural-explorer-rag-chatbot.git
cd global-cultural-explorer-rag-chatbot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run streamlit_app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## How It Works

1. The app reads `.md` and `.txt` files from the `data/` folder.
2. Markdown files are split by `## Section Title` headings.
3. Text files use the first non-empty line as the temple title.
4. The app creates TF-IDF vectors for all knowledge chunks.
5. When a user asks a question, cosine similarity finds the most relevant chunks.
6. The answer is generated from retrieved context or displayed directly when no API key is set.

## Add More Temple Files

Add a new `.txt` file inside the `data/` folder.

Use this format:

```text
Temple Name, Location

Write temple history, architecture, rituals, festivals, cultural importance, visitor etiquette, and travel notes here.
```

After adding or editing files, click **Reload knowledge base** in the app sidebar or restart Streamlit.

## Optional OpenAI Generation

The app works without OpenAI. To enable generated answers, set an API key before running the app.

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
streamlit run streamlit_app.py
```

On macOS/Linux:

```bash
export OPENAI_API_KEY="your_api_key_here"
streamlit run streamlit_app.py
```

You can optionally set a model:

```bash
export OPENAI_MODEL="gpt-4.1-mini"
```

## Example Questions

- Tell me about Tirumala Venkateswara Temple.
- Which temple is famous for Ratha Yatra and Mahaprasad?
- Explain Dravidian temple architecture.
- What should I know before visiting Kedarnath?
- Which temples are important in Odisha?
- Tell me about festivals at Meenakshi Amman Temple.

## Notes

- Do not commit API keys or secrets.
- Keep custom temple data in the `data/` folder.
- The current retrieval system is lightweight and local. It can later be upgraded to embeddings with FAISS, ChromaDB, or another vector database.

## Team members
- Charvi Gandla
- Laya Shankari
- Garela Akshaya
- Bantu Jyothi
- Madepadege Yavaneetha

  ## Team

Developed for an internship project on cultural heritage exploration using RAG.