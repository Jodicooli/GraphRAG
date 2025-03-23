import pickle
import faiss
from neo4j import GraphDatabase
from sentence_transformers import SentenceTransformer
import numpy as np
import config.settings as settings  

# Load Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Neo4j Connection
NEO4J_URI = settings.NEO4J_URI
NEO4J_USER = settings.NEO4J_USER
NEO4J_PASSWORD = settings.NEO4J_PASSWORD
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Retrieve movies & their IDs from Neo4j
def get_movies(tx):
    query = """
    MATCH (m:Movie)  
    RETURN m.movieId AS id, m.title AS title  
    LIMIT 50000
    """
    return [{"id": record["id"], "title": record["title"]} for record in tx.run(query)]

def rebuild_faiss():
    """Rebuilds FAISS index with Neo4j movie IDs and normalized embeddings."""
    with driver.session() as session:
        movies = session.read_transaction(get_movies)  

    if not movies:
        raise ValueError("No movies found! Check your Neo4j dataset.")

    # Convert movie titles to embeddings
    texts = [m["title"] for m in movies]
    embeddings = model.encode(texts)

    # Normalize embeddings for better cosine similarity search
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    # Store in FAISS with their Neo4j IDs
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension) 
    index.add(embeddings.astype('float32'))

    # Save FAISS index
    faiss.write_index(index, settings.FAISS_INDEX_PATH)

    # Save movie ID mapping
    with open("movies_list.pkl", "wb") as f:
        pickle.dump(movies, f)

    print("Successfully rebuilt FAISS index with normalized embeddings!")
