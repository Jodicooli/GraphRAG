from DAL.neo4j_handler import get_movie_info
from DAL.faiss_handler import find_similar_movies

def retrieve_context(query, limit=10):
    movie_ids = find_similar_movies(query, k=limit)
    return get_movie_info(movie_ids)