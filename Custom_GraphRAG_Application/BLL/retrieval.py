from DAL.neo4j_handler import get_movie_info
from DAL.faiss_handler import find_similar_movies

def retrieve_context(query, limit=10):
    movie_ids = find_similar_movies(query, k=20)
    movie_data = get_movie_info(movie_ids)

    movie_data_sorted = sorted(movie_data, key=lambda m: m.get("avg_rating", 0), reverse=True)

    return movie_data_sorted