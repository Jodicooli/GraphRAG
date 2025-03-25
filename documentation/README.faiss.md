# FAISS - Semantic movie search with embeddings

## Overview

[FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search) is a **vector similarity engine**.  
In this project, FAISS is used to **find semantically similar movies** based on their titles. This helps narrow down the movies to query from Neo4j.

It works by:
- Turning movie titles into **embeddings** using `sentence-transformers`
- Storing those vectors in an index
- Matching them to the user’s query using cosine similarity

This is especially useful when users ask for something like _"similar to The Matrix"_ — even if the exact title is not mentioned.

---

## Installation

To install FAISS and the sentence transformer (already in the requirements.txt file):

```bash
pip install faiss-cpu sentence-transformers
```

---

## How It Works in This Project
1. When the project starts, movie data (title, plot, actors, directors, genres, etc.) is extracted from Neo4j and combined into a textual representation for each movie.

2. The combined movie text is encoded into embeddings using the all-MiniLM-L6-v2 model from Sentence-Transformers.

3. The embeddings are indexed and stored with FAISS for efficient similarity search.

4. When a user asks a question, the query is encoded into an embedding, and the top K most similar movies are retrieved by searching the FAISS index.

```
def find_similar_movies(query, k=50, min_similarity=0.6):
    """Find similar movies using FAISS & return their Neo4j IDs with better filtering."""
    query_embedding = model.encode([query]).astype('float32')

    D, I = index.search(query_embedding, k=k)  

    relevant_movies = []
    for dist, idx in zip(D[0], I[0]):
        if idx == -1: 
            continue
        if dist < min_similarity:  
            continue

        relevant_movies.append(movies[idx]["id"])

    return relevant_movies
```
This returns a ranked list of movie IDs — which are then used to query Neo4j for rich, structured information.

---

## Why we chose FAISS
- Open-source and well-maintained by Meta

- Lightweight and fast for local development

- Perfect for semantic similarity over small to medium datasets

- Easy to rebuild/update embeddings on the fly

- Integrates well with Python and sentence-transformers

---

## Advantages of FAISS
- Free and open source

- Blazing fast: Handles large-scale vector search in milliseconds

- Great for semantic search: Combined with sentence-transformers, it enables contextual queries

- Works locally: Works without a cloud connection

---

## Disadvantages of FAISS
- Flat file-based index: Not ideal for real-time inserts or dynamic updates

- Memory-bound: Large datasets may require lots of RAM

---

## Alternatives to FAISS

| Tool           | Type             | Pros                                                | Cons                                         |
|----------------|------------------|-----------------------------------------------------|----------------------------------------------|
| **ScaNN**      | Google (Local)    | Very fast, optimized for cosine and dot product     | More complex setup, smaller community         |
| **Milvus**     | Vector Database   | Scalable, real-time inserts, supports hybrid search | Requires Docker or cloud deployment          |
| **Weaviate**   | Vector Database   | Built-in metadata filtering, modular                | Larger memory footprint, steeper learning curve |

---

## Summary
We chose FAISS because it’s lightweight, fast, and easy to integrate into a local pipeline. It's ideal for projects like this one where you want to add semantic understanding to a knowledge base without needing external APIs.

---

## References for this readme file:
- https://github.com/facebookresearch/faiss
- https://pypi.org/project/faiss-cpu/ 
- https://sbert.net/
- https://myscale.com/blog/advantages-of-faiss-benefits-features/
- https://cloud.google.com/blog/products/databases/understanding-the-scann-index-in-alloydb?hl=en
- https://milvus.io
- https://weaviate.io/