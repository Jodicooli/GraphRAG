from DAL.db_config import driver  

def get_movie_info(movie_ids):
    """Retrieve movie details efficiently using Neo4j."""
    query = """
    MATCH (m:Movie)
    WHERE m.movieId IN $movie_ids

    OPTIONAL MATCH (m)<-[:ACTED_IN]-(a:Actor)
    OPTIONAL MATCH (m)<-[:DIRECTED]-(d:Director)
    OPTIONAL MATCH (m)-[:IN_GENRE]->(g:Genre)
    OPTIONAL MATCH (u:User)-[r:RATED]->(m)

    RETURN 
        m.movieId AS id,
        COALESCE(m.title, "Unknown") AS title,
        COALESCE(m.year, "Unknown") AS year,
        COALESCE(m.plot, "No plot available") AS plot,
        COALESCE(m.languages, "Unknown") AS languages,
        COALESCE(m.countries, "Unknown") AS countries,
        COLLECT(DISTINCT COALESCE(a.name, "")) AS actors,
        COLLECT(DISTINCT COALESCE(d.name, "")) AS directors,
        COLLECT(DISTINCT COALESCE(g.name, "")) AS genres,
        COLLECT(DISTINCT {id: u.userId, name: u.name}) AS user_ratings,
        AVG(toFloat(r.rating)) AS avg_rating
    """

    with driver.session() as session:
        result = session.run(query, movie_ids=movie_ids)
        return [
            {
                "id": record["id"],
                "title": record["title"],
                "year": record["year"],
                "plot": record["plot"],
                "languages": record["languages"],
                "countries": record["countries"],
                "actors": record["actors"],
                "directors": record["directors"],
                "genres": record["genres"],
                "user_ratings": record["user_ratings"],
                "avg_rating": record["avg_rating"] if record["avg_rating"] else 0.0 
            }
            for record in result
        ]
