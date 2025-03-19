import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from config.rebuild_faiss import rebuild_faiss

FAISS_INDEX_PATH = "movie_index.faiss"

# Load FAISS index & movie data
def load_faiss_index():
    if not os.path.exists(FAISS_INDEX_PATH):  
        print("FAISS index missing! Rebuilding...")
        rebuild_faiss()  
    return faiss.read_index(FAISS_INDEX_PATH)

index = load_faiss_index()
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load movie list with IDs
with open("movies_list.pkl", "rb") as f:
    movies = pickle.load(f)

def find_similar_movies(query, k=1000):
    """Find similar movies using FAISS & return their Neo4j IDs."""
    query_embedding = model.encode([query]).astype('float32')
    D, I = index.search(query_embedding, k=k)

    return [movies[i]["id"] for i in I[0]]  