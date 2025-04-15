# Project structure overview

This project is organized to clearly separate theory, practical implementations, and documentation. Each folder is self-contained and includes everything needed to understand, install, and test a specific version of a GraphRAG system.

---

### Folder structure

```
│── 📁 Azure_Accelerator              # Implementation of GraphRAG with Azure Accelerator
│
│── 📁 Custom_GraphRAG_Application     # A custom use-case demonstrating GraphRAG integration
│
│── 📁 Customer_Support_Bot           # A bot that uses GraphRAG for answering support queries
│
│── 📁 Customer_Support_LocalBot      # A Localbot that uses GraphRAG
│
│── 📁 Employees_Slack_Bot            # Internal Slack bot powered by GraphRAG
│
│── 📁 GraphRAG_Library               # Simple implementation of the graphrag library 
│
│── 📁 Theory                         # Background theory on GraphRAG, RAG, and knowledge graphs
│
│── 📁 Transitioning_From_SQL         # Exploration of moving from traditional SQL to knowledge graphs (Stardog and Neo4j)
```

---

## Folder-by-folder breakdown

### [Theory folder](./Theory/README.md)

This folder contains all theoretical materials related to GraphRAG, including:

- Concepts and foundations of RAG and GraphRAG
- Comparisons with other retrieval methods
- Discussions about knowledge graphs, prompt engineering, and performance trade-offs
- Our final reflections, challenges, and conclusions after building multiple GraphRAG systems

You should start with this folder to understand the concept of GraphRAG and our testings.

### [Custom_GraphRAG_Application](./Custom_GraphRAG_Application/README.md) / [GraphRAG_Library](./GraphRAG_Library/README.md) / [Customer_Support_Bot](./Customer_Support_Bot/README.md) / [Employees_Slack_Bot](./Employees_Slack_Bot/README.md) / [Customer_Support_LocalBot](.Customer_Support_LocalBot/README.md)

Each of these folders contains a complete and self-contained implementation of a GraphRAG system — ranging from simple setups using libraries like graphrag to full-stack custom systems with FAISS, Neo4j, Ollama, FastAPI, and Streamlit or a bot for answering questions in Slack.

Inside each folder, you’ll find:

- A dedicated README.md explaining:

  - The goal of the implementation
  - Tools used
  - How to install and run it
- Source code organized by layers (e.g., DAL, BLL, API, Frontend)
- Setup scripts (e.g., requirements.txt)
- Optional test files or example queries

#### documentation/ (inside some implementations)

Some implementations include a nested "documentation/" folder with detailed explanations of the tools and technologies used.

Examples include:

- README.neo4j.md – how Neo4j is used, set up and more details
- README.ai.md – how OpenAI or local LLMs are integrated, what is best to use depending on the use case

These are helpful if you want to dig deeper into specific technologies or replicate just a part of the system.

These folders are independent, making it easy to run and compare them individually.

---

### [Azure Accelerator](./Azure_Accelerator/readme.md)

A complete cloud deployment of the [Azure-Samples GraphRAG Accelerator](https://github.com/Azure-Samples/graphrag-accelerator). This example shows how to use Azure OpenAI, Cognitive Search, AKS, and APIM to build a production-grade RAG pipeline.

This folder includes:

* Full deployment instructions and scripts
* Architecture diagrams and screenshots
* Notebooks for API testing and querying
* A cost analysis based on real usage

---

### [Local implementation](./Customer_Support_LocalBot/README.md)

A standalone RAG (Retrieval-Augmented Generation) pipeline running entirely offline, ideal for environments without cloud access.

This implementation includes:

* A `docker-compose.yml` for setting up local services
* Local vector database using **ChromaDB**
* Embedding and generation via **DeepSeek LLMs** or **OpenAI**
* FastAPI backend and Streamlit frontend, runnable locally

---

### [Transitioning from SQL](./Transitioning_From_SQL/README.md)

A practical guide for teams moving from traditional relational databases to knowledge graphs. This folder demonstrates how to migrate SQL-based systems to graph databases (Stardog and Neo4j) while implementing GraphRAG capabilities.

---
