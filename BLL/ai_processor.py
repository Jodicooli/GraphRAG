import ollama

def build_graph_paths(movies):
    """Constructs knowledge graph relationships from movie data."""
    paths = []
    for m in movies:
        movie = m["title"]
        for actor in m.get("actors", []):
            paths.append(f"{actor} —[:ACTED_IN]→ {movie}")
        for director in m.get("directors", []):
            paths.append(f"{director} —[:DIRECTED]→ {movie}")
        for genre in m.get("genres", []):
            paths.append(f"{movie} —[:IN_GENRE]→ {genre}")
        for language in m.get("languages", []):
            paths.append(f"{movie} —[:HAS_LANGUAGE]→ {language}")
        for country in m.get("countries", []):
            paths.append(f"{movie} —[:ORIGINATES_FROM]→ {country}")
        for user in m.get("user_ratings", []):
            name = user.get("name", f"User {user.get('id')}")
            paths.append(f"{name} —[:RATED]→ {movie}")
    return "\n".join(paths)

def generate_response(answer, query):
    """Generates a precise and structured response using a local LLM via Ollama."""

    system_msg = """
        You are an expert AI assistant for a movie knowledge graph. Your goal is to provide **precise, relevant, and structured answers**.
        
        As soon as something is asked with connections, relationships, or similar you should put the tag "<SHOW_GRAPH>" as the first word in your response.

        ### Rules:
        1. **Only include movies that are directly related to the user's query**.
        2. **Avoid unrelated information**—do not list extra movies unless they are relevant.
        3. **Do not guess**. If the information is missing, say **"I don't have that information."**
        4. **Use structured formatting** for clarity.
        """

    # Format structured data
    movie_details = "\n".join([
        f"""{i+1}. *{m['title']}*
        • Year: {m.get('year', 'N/A')}
        • Plot: {m.get('plot', 'N/A')}
        • Languages: {', '.join(m.get('languages', [])) or 'N/A'}
        • Countries: {', '.join(m.get('countries', [])) or 'N/A'}
        • Genres: {', '.join(m.get('genres', []))}
        • Directed by: {', '.join(m.get('directors', []))}
        """ for i, m in enumerate(answer.get("movies", []))
    ])

    graph_paths = build_graph_paths(answer["movies"])

    if "country" in query.lower():
        focus_field = "countries"
    elif "director" in query.lower():
        focus_field = "directors"
    elif "actor" in query.lower():
        focus_field = "actors"
    elif "genre" in query.lower():
        focus_field = "genres"
    elif "language" in query.lower():
        focus_field = "languages"
    elif "plot" in query.lower():
        focus_field = "plot"
    elif "rating" in query.lower():
        focus_field = "user ratings"
    elif "year" in query.lower():
        focus_field = "year"
    elif "title" in query.lower():
        focus_field = "title"
    elif "average" in query.lower():
        focus_field = "average rating"
    elif "user" in query.lower():
        focus_field = "user ratings"
    else:
        focus_field = "general information"

    prompt = f"""
    User Query: "{query}"

    ### Relevant Field: {focus_field}

    ### Available Movie Data:
    {movie_details}

    ### Graph-Based Relationships:
    {graph_paths}

    **Instructions:**
    - Focus on `{focus_field}` when answering.
    - Do **not** include unrelated movies or fields.
    - Use structured formatting.
    """

    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']
