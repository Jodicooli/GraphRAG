# GraphRAG: AI-Powered Movie Q&A with Neo4j + FAISS + Local LLMs + Streamlit

## Overview
GraphRAG (Graph-based Retrieval-Augmented Generation) is a smart AI system that combines in our project:

- **Neo4j**: A graph database for structured movie knowledge (movies, actors, genres, users, ratings, etc.)

- **FAISS**: For fast semantic search over movie embeddings

- **Ollama + llama3**: A local LLM that generates rich, graph-aware answers

- **Streamlit**: A simple, friendly UI to ask natural language movie questions

This system dynamically retrieves knowledge from both **graph-based** and **vector-based** search, ensuring **more relevant** and **accurate AI responses**.

---

## Folder Structure
```
GraphRAG_Project/
│── 📁 dal/                     # Data Access Layer (DAL)
│   ├── faiss_handler.py        # Handles FAISS operations
│   ├── neo4j_handler.py        # Handles Neo4j queries dynamically
│   ├── db_config.py            # Centralized database configuration
│
│── 📁 bll/                     # Business Logic Layer (BLL)
│   ├── retrieval.py            # Dynamically retrieves data from FAISS & Neo4j
│   ├── ai_processor.py         # Interacts with LLM via Ollama
│
│── 📁 api/                     # API Layer (FastAPI)
│   ├── main.py                 # API endpoints
│
│── 📁 frontend/                # Frontend Layer (Streamlit)
│   ├── app.py                  # UI for user interaction
│
│── 📁 config/                  # Configurations
│   ├── settings.py             # Centralized settings (DB URIs)
│   ├── rebuild_faiss.py        # Rebuilds the FAISS in case it is missing
│   ├── .env                    # stores the credentials of the databse 
│
│── 📁 documentation/           # Documentation
│   ├── README.ai.md            # documentation about OpenAI and Ollama
│   ├── README.faiss.md         # documentation about FAISS
│   ├── README.fastapi.md       # documentation about FastAPI
│   ├── README.neo4j.md         # documentation about Neo4j and the database database
│   ├── README.streamlit.md     # documentation about Streamlit
│
│── 📁 db_backup_file/          # Backup file for the database
│   ├── recommandations-50.dump # .dump file to recreate the database (for Neo4j)
│
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## Documentations
All documentation related to the technologies used in this project can be found in the documentation/ folder. For each technology, we created a separate README.md file that includes:

- A short explanation of what the tool is

- Installation steps

- How it is used in this specific GraphRAG project

- Where it make sence some code examples

- Advantages & Disadvantages

- Alternatives 

These technology-specific files are:

- README.neo4j.md: Graph database for modeling movie data

- README.faiss.md: Semantic search using embeddings

- README.fastapi.md: Lightweight backend API

- README.streamlit.md: Python-based UI for interaction

- README.ai.md: OpenAI and Ollama (LLM-based response generation)

---

## How we created this application
We followed a modular approach to build the full-stack AI system from scratch:

- **Data**: We started with a .dump file, which we found on https://neo4j.com/docs/getting-started/appendix/example-data/ containing movie ratings and metadata (imported into Neo4j).

- **FAISS Index**: Created using SentenceTransformers to store vector representations of movie titles for similarity search.

- **Backend (FastAPI)**: Handles API queries and communicates with both FAISS and Neo4j.

- **LLM Reasoning (Ollama)**: Generates answers using local models (like llama3) based on graph knowledge and embeddings.

- **Frontend (Streamlit)**: Enables natural user interaction with graph-based visualizations and charts.

- **Documentations**: We documented each layer separately to make it easy for others to reuse or learn from our approach.

The structure is clean and separated into DAL, BLL, API, Frontend, and Config, making it easy to maintain and scale.

---

## Setup & Installation

### 1. Create your database
1. Access the site: [https://neo4j.com/](https://neo4j.com/)

2. Click on **Get Started Free** and create an account

3. Create a new instance if you do not have one yet by clicking on **Create instance**

4. You can now **import** your data from a **data source** or directly click on the three dots next to the current instance, select **Backup & restore** and browse for your **.dump file**. The dump file for the movie dataset is in the folder: **db_backup_file**

5. Create a **.env** file in the **config** folder and put your database URI, username, and password with the following variable names: NEO4J_URI, NEO4J_USER and NEO4J_PASSWORD. 
![.env file](images/env_file.png)

### 2. Make sure Ollama is installed (https://ollama.com/download/windows) and run the following two commands
```bash
ollama pull llama3
ollama run llama3
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Backend API (FastAPI)
```bash
uvicorn api.main:app --reload
```

### 5. Start the Frontend (Streamlit UI)
```bash
streamlit run frontend/app.py
```

---

## How It Works
1. **User asks a question** via the Streamlit UI or API.

2. **FAISS retrieves similar past questions** from stored embeddings.

3. **Neo4j dynamically retrieves graph-based knowledge** from the Movie dataset.

4. **Ollama (with llama3) generates an AI response** using both FAISS & Neo4j context.

5. **Answer is returned to the user** through the frontend or API.

---

## Example API Calls
### Ask a Question
```bash
curl "http://127.0.0.1:8000/ask?query=Who+is+Harry+Potter?"
```

### Test the API in Browser
Open `http://127.0.0.1:8000/docs` in your browser to use the interactive Swagger UI.

---

## Some features of this application
- Semantic similarity search (FAISS + SentenceTransformers)

- Rich graph relationships: movies, genres, actors, users, ratings

- Real-time API and UI

- Works offline with local LLMs (Ollama)

---

## Conclusion of this application created with Neo4j, FAISS, FastAPI, Streamlit and Ollama/OpenAI

This project demonstrates how you can **fully implement** a GraphRAG system **from scratch** without relying on any pre-packaged or proprietary solution. While pre-packaged tools offer shortcuts, building it yourself brings:

- A **deeper understanding** of how knowledge retrieval, vector search, and reasoning actually work

- **Full customization** of your graph structure, prompt engineering, reasoning paths, and UI

- **Transparency and debugging** freedom

However, we also noticed some **limitations**:

- The system can be **slow**, especially when the reasoning becomes complex or when the local LLM is under heavy load.

- Local LLMs like llama3 (via Ollama) are impressive but sometimes struggle with very **nuanced** or **long queries**.

- Query **performance depends heavily on database size**, indexing, and memory usage.

- Depending on the LLM you use, it can be a little **expensive** and you have to keep an eye on the costs. At the beginning we used an API key from OpenAI. After only few days using to code the application and debug, we already had a bill of over 6 dollars.

That said, this architecture is ideal for learning, prototyping, and local use cases — especially when privacy, customization, and cost control matter.

---

## Experiments and Challenges

Throughout the development of this GraphRAG system, we tested various approaches, models, and configurations. While each experiment provided valuable insights, not all solutions were ideal. Here’s what we tried and the challenges we encountered:

### 1. OpenAI vs. Local LLMs
- OpenAI’s models (GPT-4) were significantly more accurate and reliable but came with a cost. Even during early development and debugging, we accumulated a bill of over $6 in just a few days.

- Local LLMs via Ollama (e.g., Llama3, Mistral, and others) were free and private but varied in speed, accuracy, and reasoning ability. Some models struggled with long or nuanced queries.

### 2. Multi-Hop Reasoning
- Initially, we tested multi-hop reasoning to improve context understanding. However, this made the system extremely slow, especially with complex queries.

- Instead of improving responses, it often overcomplicated the reasoning chain, leading to incoherent or redundant answers.

### 3. Different LLMs in Ollama (Mistral, Llama3, etc.)
- Mistral was fast but sometimes less accurate.

- Llama3 performed better but is a little slower, especially with longer reasoning chains.

- Compared to OpenAI, local models required much more prompt tuning to produce useful responses.

### 4. Dataset size and impact on performance
- We experimented with different datasets, including a Stack Overflow dataset.

- Larger datasets significantly increased response time, highlighting the importance of efficient indexing and memory management.

### 5. The challenge of prompt engineering
- We spent several days testing hundreds of different prompts, trying to optimize responses.

- When switching from OpenAI to Ollama, we often had to rewrite and fine-tune prompts just to get coherent answers.

- Small changes in phrasing could completely alter the model’s response quality.

---

### Key Takeaways
- OpenAI is expensive but more reliable and accurate.

- Local LLMs are cheaper but require extensive prompt tuning and optimization.

- Multi-hop reasoning wasn’t always beneficial and often made the system slower.

- Dataset size significantly affects performance and should be carefully managed.

- While these experiments weren’t always successful, they provided critical insights into optimizing a GraphRAG system for real-world applications. 