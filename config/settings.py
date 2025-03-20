import os
from dotenv import load_dotenv

# Charger les variables d’environnement depuis un fichier .env
load_dotenv("config/.env")

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Neo4j Database Config
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# FAISS Configuration
FAISS_INDEX_PATH = "movie_index.faiss"
