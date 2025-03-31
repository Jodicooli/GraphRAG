import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
from dal.neo4j_handler import get_related_info

load_dotenv("config/.env")

# Load OpenAI API key
openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)

# Load FAISS index
index = faiss.read_index("index/faiss_graph_index.bin")
with open("index/graph_chunks.pkl", "rb") as f:
    text_chunks = pickle.load(f)

# Embed model
model = SentenceTransformer("all-MiniLM-L6-v2")

def query_llm(question):
    # 1. Get top FAISS chunk
    q_emb = model.encode([question])
    D, I = index.search(q_emb, k=3)
    faiss_results = [text_chunks[i] for i in I[0]]

    # 2. Get Neo4j info
    # Extract the most likely topic (assume keyword for now)
    keyword = question.split()[0].capitalize()
    graph_context = get_related_info(keyword)

    # 3. Build prompt
    context = "\n\n".join(faiss_results)
    prompt = f"""
        You are a helpful customer support assistant. Use the following context to answer the user's question as clearly and politely as possible.
        If you don't know the answer, say "I don't have that information."
        If the question is not related to the context, say "I can't help you with that."
        If the question is too vague, ask for clarification.

        Graph Knowledge:
        {graph_context}

        Text Knowledge:
        {context}

        User Question:
        {question}

        Answer:
        """

    # 4. Query OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
