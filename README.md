# Project structure overview

This project is organized to clearly separate theory, practical implementations, and documentation. Each folder is self-contained and includes everything needed to understand, install, and test a specific version of a GraphRAG system.

---

## Folder-by-folder breakdown

### Theory folder

This folder contains all theoretical materials related to GraphRAG, including:

- Concepts and foundations of RAG and GraphRAG

- Comparisons with other retrieval methods

- Discussions about knowledge graphs, prompt engineering, and performance trade-offs

- Our final reflections, challenges, and conclusions after building multiple GraphRAG systems

You should start with this folder to understand the concept of GraphRAG and our testings.

### Custom_GraphRAG_Application / GraphRAG_Library / etc. folders

Each of these folders contains a complete and self-contained implementation of a GraphRAG system — ranging from simple setups using libraries like graphrag to full-stack custom systems with FAISS, Neo4j, Ollama, FastAPI, and Streamlit.

Inside each folder, you’ll find:

- A dedicated README.md explaining:

    - The goal of the implementation

    - Tools used

    - How to install and run it

- Source code organized by layers (e.g., DAL, BLL, API, Frontend)

- Environment files or setup scripts (e.g., .env.example, requirements.txt)

- Optional test files or example queries

These folders are independent, making it easy to run and compare them individually.

### documentation/ (inside some implementations)

Some implementations include a nested documentation/ folder with detailed explanations of the tools and technologies used.

Examples include:

- README.neo4j.md – how Neo4j is used, set up and more details

- README.ai.md – how OpenAI or local LLMs are integrated, what is best to use depending on the use case

These are helpful if you want to dig deeper into specific technologies or replicate just a part of the system.

---
