import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from pathlib import Path
from neo4j import GraphDatabase
from dal.neo4j_handler import get_driver

driver = get_driver()

def get_graph_chunks():
    with driver.session() as session:
        query = """
        MATCH (t:Topic)-[:COVERS|RELATED_TO|CONTACT_VIA]->(n)
        OPTIONAL MATCH (n)-[:ALLOWS|APPLIES_TO]->(d)
        RETURN t.name AS topic, collect(DISTINCT n.name) + collect(DISTINCT d.name) AS info
        """
        result = session.run(query)
        chunks = []
        for row in result:
            topic = row["topic"]
            info_list = row["info"]
            if not info_list:
                continue
            text = f"Topic: {topic}. Related: {', '.join(info_list)}."
            chunks.append(text)
        return chunks

# Step 1: Extract from Neo4j
graph_chunks = get_graph_chunks()
print(f"Retrieved {len(graph_chunks)} graph chunks from Neo4j.")

# Step 2: Embed with SentenceTransformers
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(graph_chunks, show_progress_bar=True)

# Step 3: Build FAISS index
dim = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# Step 4: Save index + chunks
Path("index").mkdir(exist_ok=True)
faiss.write_index(index, "index/faiss_graph_index.bin")
with open("index/graph_chunks.pkl", "wb") as f:
    pickle.dump(graph_chunks, f)

print("FAISS index from Neo4j created and saved.")
