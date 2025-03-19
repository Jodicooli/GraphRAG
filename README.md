# 🧠 GraphRAG: AI-Powered Q&A with Neo4j + FAISS + GPT-4

## 🚀 Overview
GraphRAG (Graph-based Retrieval-Augmented Generation) is an advanced AI system that:
- Uses **Neo4j (Graph Database)** for structured knowledge retrieval.
- Uses **FAISS (Vector Database)** for semantic similarity search.
- Uses **GPT-4** for generating AI-powered answers.

This system dynamically retrieves knowledge from both **graph-based** and **vector-based** search, ensuring **more relevant** and **accurate AI responses**.

---

## 📂 Folder Structure
```
GraphRAG_Project/
│── 📁 dal/               # Data Access Layer (DAL)
│   ├── faiss_handler.py  # Handles FAISS operations
│   ├── neo4j_handler.py  # Handles Neo4j queries dynamically
│   ├── db_config.py      # Centralized database configuration
│
│── 📁 bll/               # Business Logic Layer (BLL)
│   ├── retrieval.py      # Dynamically retrieves data from FAISS & Neo4j
│   ├── ai_processor.py   # AI logic (GPT-4 interaction)
│
│── 📁 api/               # API Layer (FastAPI)
│   ├── main.py           # API endpoints
│
│── 📁 frontend/          # Frontend Layer (Streamlit)
│   ├── app.py            # UI for user interaction
│
│── 📁 config/            # Configurations
│   ├── settings.py       # Centralized settings (API keys, DB URIs)
│
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## 🛠️ Setup & Installation

### ➕ 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### ➕ 2. Start the Backend API (FastAPI)
```bash
uvicorn api.main:app --reload
```

### ➕ 3. Start the Frontend (Streamlit UI)
```bash
streamlit run frontend/app.py
```

---

## 🚀 How It Works
1. **User asks a question** via the Streamlit UI or API.
2. **FAISS retrieves similar past questions** from stored embeddings.
3. **Neo4j dynamically retrieves graph-based knowledge** from the StackOverflow dataset.
4. **GPT-4 generates an AI response** using both FAISS & Neo4j context.
5. **Answer is returned to the user** through the frontend or API.

---

## 🔍 Example API Calls
### 🔹 Ask a Question
```bash
curl "http://127.0.0.1:8000/ask?query=How+to+optimize+database+indexing?"
```

### 🔹 Test the API in Browser
Open `http://127.0.0.1:8000/docs` in your browser to use the interactive Swagger UI.

---

## 🚀 Future Improvements
- ✅ **Deploy API & UI to the cloud (AWS, Render, Railway)**
- ✅ **Improve Neo4j retrieval with multi-hop queries**
- ✅ **Add caching for faster responses**
- ✅ **Fine-tune GPT-4 prompts for better responses**

---

## 👨‍💻 Contributors
- **Adriano Dias** 
- **Johanna S.** 
- **Lorenzo De Ieso** 
- **Luana Ramirez**

---

🚀 **Happy Coding! Let me know if you need any improvements!** 🔧

