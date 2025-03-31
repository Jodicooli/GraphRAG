from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from llm.response_generator import query_llm
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Allow frontend to call this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for testing. You can restrict later.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def serve_index():
    return FileResponse(os.path.abspath("frontend/index.html"))

@app.get("/ask")
def ask(query: str):
    answer = query_llm(query)
    return {"question": query, "answer": answer}