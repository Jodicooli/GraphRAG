import ollama

def generate_response(answer, query):
    """Generates a rich, helpful, accurate response using a local LLM via Ollama."""

    # Step 1: Sort and format knowledge
    movies_sorted = sorted(answer["movies"], key=lambda x: x.get("avg_rating", 0), reverse=True)
    knowledge = "\n".join([
        f"{i+1}. 🎬 *{m['movie']}*\n   • ⭐ Avg Rating: {round(m.get('avg_rating', 0), 2)}\n   • 🎭 Genres: {', '.join(m.get('genres', []))}\n   • 🎬 Directed by: {', '.join(m.get('directors', []))}\n   • 👥 Rated by: {len(m.get('user_ratings', []))} users"
        for i, m in enumerate(movies_sorted)
    ])
    
    graph_paths = build_graph_paths(answer["movies"])

    # Step 2: Define system behavior clearly
    system_msg = """
        You are part of a GraphRAG system using Neo4j as the source of structured movie knowledge.
        Your task is to explain movie relationships using graph concepts.

        "Never explain how to write queries or how graphs work.\n"
        "Instead, use the graph-based knowledge already retrieved to answer clearly with real values (movie titles, actor names, etc).\n"

        Each movie node may be connected to:
        - (Actor) via ACTED_IN
        - (Director) via DIRECTED
        - (Genre) via IN_GENRE
        - (User) via RATED

        "You SHOULD recommend visualizations using <SHOW_GRAPH> or <SHOW_BAR_CHART> when helpful. Don’t say you can’t — just trigger the tags at the top of the message and than add your text."
        When a user asks about people, genres, or connections:
        1. Extract those from the given data.
        2. Mention relationships explicitly like: Actor —[:ACTED_IN]→ Movie.
        3. Include <SHOW_GRAPH> if the graph view would help.
        4. If top movies are compared by rating, also include <SHOW_BAR_CHART>.

        Never say “no data found” unless you’ve verified none exist in the structured input.
        """


    # Step 3: Build user prompt
    prompt = f"""
        Here is structured movie knowledge retrieved from a graph database (via GraphRAG):

        {knowledge}

        🔗 Graph relationships:
        {graph_paths}

        User Question: {query}

        Please reason step-by-step using the relationships above. If a graph would help, add <SHOW_GRAPH>. If rating comparisons would help, add <SHOW_BAR_CHART>.
        """

    # Step 4: Generate
    response = ollama.chat(
        model='mistral',
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']

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
