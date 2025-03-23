import ollama

def perform_hop_reasoning(movies, query):
    """Performs multiple hop reasoning on the movie data."""
    
    reasoning_prompt = f"""
    Analyze the following movie data using multiple hop reasoning:
    1. First hop: Direct relationships (movie->genre, movie->director, etc.)
    2. Second hop: Indirect relationships (actor->movie->genre, director->movie->rating)
    3. Third hop: Complex patterns (actor->multiple movies->common genres)
    
    Provide structured reasoning steps that:
    1. Identify relevant entities in the query
    2. Follow relationship paths
    3. Draw conclusions from patterns
    
    Data to analyze: {movies}
    Query: {query}
    """
    
    reasoning_response = ollama.chat(
        model='mistral',
        messages=[
            {"role": "user", "content": reasoning_prompt}
        ]
    )
    
    return reasoning_response['message']['content']

def generate_response(answer, query):
    """Generates a rich, helpful, accurate response using a local LLM via Ollama."""

    # Define system behavior with explicit visualization rules
    system_msg = """
    You are part of a GraphRAG system using Neo4j. Follow these strict rules:

    1. ALWAYS start your response with visualization tags when applicable:
       - Use <SHOW_GRAPH> for relationship visualizations
       - Use <SHOW_BAR_CHART> for rating comparisons
    
    2. REQUIRED tag usage:
       - When comparing 2+ movies/actors/directors → <SHOW_BAR_CHART>
       - When explaining relationships/connections → <SHOW_GRAPH>
    
    3. Format:
       - First line: visualization tags
       - Second line: Clear answer based on reasoning
       - Third line onwards: Supporting details

    Never skip tags when relationships or comparisons are involved.
    """

    # Force visualization tags based on query type
    visualization_tags = []
    if any(word in query.lower() for word in ['visualize', 'show', 'connection', 'relationship', 'between']):
        visualization_tags.append("<SHOW_GRAPH>")
    if any(word in query.lower() for word in ['compare', 'rating', 'best', 'top', 'versus', 'vs']):
        visualization_tags.append("<SHOW_BAR_CHART>")

    # Sort and format knowledge
    movies_sorted = sorted(answer["movies"], key=lambda x: x.get("avg_rating", 0), reverse=True)
    knowledge = "\n".join([
        f"{i+1}. 🎬 *{m['movie']}*\n   • Avg Rating: {round(m.get('avg_rating', 0), 2)}\n   • Genres: {', '.join(m.get('genres', []))}\n   • Directed by: {', '.join(m.get('directors', []))}\n   • Rated by: {len(m.get('user_ratings', []))} users"
        for i, m in enumerate(movies_sorted)
    ])
    
    graph_paths = build_graph_paths(answer["movies"])
    
    # Perform multiple hop reasoning
    reasoning_results = perform_hop_reasoning(answer["movies"], query)

    # Build final response with forced visualization tags
    final_response = "\n".join(visualization_tags) + "\n" if visualization_tags else ""
    
    # Generate content with Ollama
    prompt = f"""
    Based on the following information, provide a detailed answer:
    
    Question: {query}
    
    Multiple Hop Reasoning Results:
    {reasoning_results}

    Structured Knowledge:
    {knowledge}

    Graph Relationships:
    {graph_paths}
    """
    
    response = ollama.chat(
        model='mistral',
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )
    
    # Combine tags with response
    final_response += response['message']['content']
    return final_response

def build_graph_paths(movies):
    paths = []
    for m in movies:
        movie = m["movie"]
        for actor in m["actors"]:
            paths.append(f"{actor} —[:ACTED_IN]→ {movie}")
        for director in m["directors"]:
            paths.append(f"{director} —[:DIRECTED]→ {movie}")
        for genre in m["genres"]:
            paths.append(f"{movie} —[:IN_GENRE]→ {genre}")
        for user in m["user_ratings"]:
            name = user.get("name", f"User {user.get('id')}")
            paths.append(f"{name} —[:RATED]→ {movie}")
    return "\n".join(paths)