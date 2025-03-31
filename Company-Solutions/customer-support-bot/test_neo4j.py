from dal.neo4j_handler import get_related_info

if __name__ == "__main__":
    topic = "Returns"
    result = get_related_info(topic)
    print(result)
