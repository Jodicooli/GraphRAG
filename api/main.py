from fastapi import FastAPI
from BLL.retrieval import retrieve_context

app = FastAPI()

@app.get("/ask")
def ask_question(query: str):
    """Handles user queries & fetches movie relationships using GraphRAG."""
    response = retrieve_context(query)
    return {"movies": response}
