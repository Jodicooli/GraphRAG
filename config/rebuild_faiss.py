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
        OPTIONAL MATCH (m)<-[:ACTED_IN]-(a:Actor)
        OPTIONAL MATCH (m)<-[:DIRECTED]-(d:Director)
        OPTIONAL MATCH (m)-[:IN_GENRE]->(g:Genre)

        RETURN
            m.movieId AS id,
            m.title AS title,
            m.year AS year,
            m.languages AS languages,
            m.countries AS countries,
            m.plot AS plot,
            COLLECT(DISTINCT coalesce(a.name, "")) AS actors,
            COLLECT(DISTINCT coalesce(d.name, "")) AS directors,
            COLLECT(DISTINCT coalesce(g.name, "")) AS genres

        LIMIT 50000
    """
    # record.data() returns a dict of all returned fields
    return [record.data() for record in tx.run(query)]

def rebuild_faiss():
    with driver.session() as session:
        movies = session.read_transaction(get_movies)

    if not movies:
        raise ValueError("No movies found! Check your Neo4j dataset.")

    # Build a textual representation for each movie
    texts = []
    for m in movies:
        # Safely handle None values
        title = m.get("title", "")
        plot = m.get("plot", "")
        year = m.get("year", "")
        actors = ", ".join(m.get("actors", []))
        directors = ", ".join(m.get("directors", []))
        genres = ", ".join(m.get("genres", []))
        imdb_rating = m.get("imdbRating", "")
        imdb_votes = m.get("imdbVotes", "")

        # Combine everything into a single text block
        movie_text = f"""
        Title: {title}
        Year: {year}
        Plot: {plot}
        Actors: {actors}
        Directors: {directors}
        Genres: {genres}
        IMDb Rating: {imdb_rating}
        IMDb Votes: {imdb_votes}
        """
        texts.append(movie_text.strip())

    # Encode with SentenceTransformer
    embeddings = model.encode(texts, show_progress_bar=True)
    # Normalize embeddings
    embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings.astype('float32'))

    # Save FAISS index
    faiss.write_index(index, settings.FAISS_INDEX_PATH)

    # Save movie data (including IDs + all details)
    with open("movies_list.pkl", "wb") as f:
        pickle.dump(movies, f)

    print("Successfully rebuilt FAISS index!")