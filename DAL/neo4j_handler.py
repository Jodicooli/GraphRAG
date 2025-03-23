from DAL.db_config import driver  

def get_movie_info(movie_ids):
    """Retrieve movie relationships using movie IDs (GraphRAG)."""
    query = """
    MATCH (m:Movie)
    WHERE m.movieId IN $movie_ids

    OPTIONAL MATCH (m)<-[:ACTED_IN]-(a:Actor)
    OPTIONAL MATCH (m)<-[:DIRECTED]-(d:Director)
    OPTIONAL MATCH (m)-[:IN_GENRE]->(g:Genre)
    OPTIONAL MATCH (u:User)-[r:RATED]->(m)

    RETURN 
    m.movieId AS id,
    m.title AS movie,
    COLLECT(DISTINCT a.name) AS actors,
    COLLECT(DISTINCT d.name) AS directors,
    COLLECT(DISTINCT g.name) AS genres,
    COLLECT(DISTINCT {id: u.userId, name: u.name}) AS user_ratings,
    COLLECT(DISTINCT {
        user: u.name,
        movie: m.title,
        actor: a.name,
        director: d.name,
        genre: g.name,
        rating: r.rating
    }) AS graph_paths,
    AVG(toFloat(r.rating)) AS avg_rating
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
                "user_ratings": record["user_ratings"],
                "avg_rating": record["avg_rating"]  
            }
            for record in result
        ]
