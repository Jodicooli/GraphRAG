# GraphRAG: AI-Powered Movie Q&A with Neo4j + FAISS + Local LLMs

## Overview
GraphRAG (Graph-based Retrieval-Augmented Generation) is a smart AI system that combines:
- **Neo4j**: A graph database for structured movie knowledge (movies, actors, genres, users, ratings, etc.)
- **FAISS**: For fast semantic search over movie embeddings
- **Ollama + Mistral**: A local LLM that generates rich, multi-hop, graph-aware answers
- **Streamlit**: A simple, friendly UI to ask natural language movie questions

This system dynamically retrieves knowledge from both **graph-based** and **vector-based** search, ensuring **more relevant** and **accurate AI responses**.

---

## Folder Structure
```
GraphRAG_Project/
│── 📁 dal/               # Data Access Layer (DAL)
│   ├── faiss_handler.py  # Handles FAISS operations
│   ├── neo4j_handler.py  # Handles Neo4j queries dynamically
│   ├── db_config.py      # Centralized database configuration
│
│── 📁 bll/               # Business Logic Layer (BLL)
│   ├── retrieval.py      # Dynamically retrieves data from FAISS & Neo4j
│   ├── ai_processor.py   # Interacts with LLM via Ollama
│
│── 📁 api/               # API Layer (FastAPI)
│   ├── main.py           # API endpoints
│
│── 📁 frontend/          # Frontend Layer (Streamlit)
│   ├── app.py            # UI for user interaction
│
│── 📁 config/            # Configurations
│   ├── settings.py       # Centralized settings (DB URIs)
│
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Make sure Ollama is installed (https://ollama.com/download/windows) and run the following command
```bash
ollama run mistral
```

### 3. Start the Backend API (FastAPI)
```bash
uvicorn api.main:app --reload
```

### 4. Start the Frontend (Streamlit UI)
```bash
streamlit run frontend/app.py
```

---

## How It Works
1. **User asks a question** via the Streamlit UI or API.
2. **FAISS retrieves similar past questions** from stored embeddings.
3. **Neo4j dynamically retrieves graph-based knowledge** from the StackOverflow dataset.
4. **Ollama (with Mistral) generates an AI response with multi-hop explanation** using both FAISS & Neo4j context.
5. **Answer is returned to the user** through the frontend or API.

---

## Example API Calls
### Ask a Question
```bash
curl "http://127.0.0.1:8000/ask?query=How+to+optimize+database+indexing?"
```

### Test the API in Browser
Open `http://127.0.0.1:8000/docs` in your browser to use the interactive Swagger UI.

---

## Features
- Semantic similarity search (FAISS + SentenceTransformers)
- Multi-hop reasoning over movie data (via GraphRAG)
- Rich graph relationships: movies, genres, actors, users, ratings
- Real-time API and UI
- Works offline with local LLMs (Ollama)