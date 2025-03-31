import os
from neo4j import GraphDatabase

from config import settings

# Neo4j Connection
NEO4J_URI = settings.NEO4J_URI
NEO4J_USER = settings.NEO4J_USER
NEO4J_PASSWORD = settings.NEO4J_PASSWORD

# Neo4j Driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def get_driver():
    """Get the Neo4j driver."""
    return driver

def get_related_info(topic):
    with driver.session() as session:
        query = """
        MATCH (t:Topic {name: $topic})-[:COVERS|RELATED_TO|CONTACT_VIA]->(related)
        OPTIONAL MATCH (related)-[r2]->(sub)
        RETURN t.name AS topic,
               collect(DISTINCT related.name) AS related_info,
               collect(DISTINCT sub.name) AS sub_info
        """
        result = session.run(query, topic=topic)
        row = result.single()

        if not row:
            return f"No information found for topic: {topic}"

        topic = row["topic"]
        related = row["related_info"]
        sub = row["sub_info"]

        return (
            f"**Topic**: {topic}\n"
            f"Related: {', '.join(related)}\n"
            f"Details: {', '.join([s for s in sub if s])}"
        )