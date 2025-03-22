# FastAPI - Lightweight API for GraphRAG Backend

## What is FastAPI?

[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance Python web framework for building APIs. It’s built on top of **Starlette** and **Pydantic**, making it fast, simple, and easy to use — perfect for rapid prototyping and production-level apps alike.

In this project, FastAPI powers the backend API that connects the **Frontend UI**, **FAISS retrieval**, and **Neo4j graph database**.

---

## Installation

Install FastAPI and a server (we use `uvicorn` for development):

```bash
pip install fastapi uvicorn
```

## How It’s Used in This Project
We use FastAPI to define a simple route that accepts a movie-related question and returns a structured response. The endpoint connects all retrieval components (FAISS + Neo4j) and returns data to the frontend.

```
from fastapi import FastAPI
from BLL.retrieval import retrieve_context

app = FastAPI()

@app.get("/ask")
def ask_question(query: str):
    """Handles user queries & fetches movie relationships using GraphRAG."""
    response = retrieve_context(query)
    return {"movies": response}
```

When you call this /ask endpoint with a query like What is the best crime movie?, it returns a JSON response with relevant movie information pulled from both vector and graph-based retrieval.

---

## Running the API
To run the API locally: ```bash uvicorn api.main:app --reload ```
Then go to http://localhost:8000/docs for interactive Swagger documentation.


## Why We Used FastAPI

- **Fast & efficient**: Built on ASGI for high-performance APIs.
- **Pythonic**: Clean and readable syntax.
- **Async support**: Easily handle I/O operations like database calls.
- **Automatic docs**: OpenAPI/Swagger docs available at `/docs`.
- **Easy integration**: Works well with Neo4j, FAISS, and local LLMs like Ollama.

---

### Advantages of FastAPI


---

### Disadvantages of FastAPI



---

### Alternatives to FastAPI

---

### Summary
