from DAL.db_config import driver  

from DAL.db_config import driver  

def get_movie_info(movie_ids):
    """Retrieve movie relationships using movie IDs (GraphRAG)."""
    query = """
    MATCH (m:Movie)
    WHERE m.movieId IN $movie_ids
    OPTIONAL MATCH (m)<-[:ACTED_IN]-(a:Actor)
    OPTIONAL MATCH (m)<-[:DIRECTED]-(d:Director)
    OPTIONAL MATCH (m)-[:BELONGS_TO]->(g:Genre)
    OPTIONAL MATCH (m)<-[:RATED]-(u:User)
    RETURN 
        m.movieId AS id,
        m.title AS movie,
        COLLECT(DISTINCT a.name) AS actors,
        COLLECT(DISTINCT d.name) AS directors,
        COLLECT(DISTINCT g.name) AS genres,
        COLLECT(DISTINCT u.userId) AS user_ratings
    """

    with driver.session() as session:
        result = session.run(query, movie_ids=movie_ids)
        return [
            {
                "id": record["id"],
                "movie": record["movie"],
                "actors": record["actors"],
                "directors": record["directors"],
                "genres": record["genres"],
                "user_ratings": record["user_ratings"] 
            }
            for record in result
        ]
