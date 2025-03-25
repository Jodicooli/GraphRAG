from fastapi import FastAPI
from BLL.retrieval import retrieve_context

app = FastAPI()

@app.get("/ask")
def ask_question(query: str):
    """Handles user queries & fetches relevant information in a structured format."""
    response = retrieve_context(query)
    return {"movies": response}
