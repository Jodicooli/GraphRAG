import json
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
    You are an expert AI assistant for a movie knowledge graph. Your job is to provide **precise, relevant, and structured answers** to user questions.
    
    As soon as something is asked with connections, relationships, or similar you should put the tag "<SHOW_GRAPH>" as the first word in your response.
    As soon as something is asked with a list of items, or a chart, or a rating you should put the tag "<SHOW_BAR_CHART>" as the first word in your response.

    **Rules:**
    1. your answer shhould answer the user's question. Add extra information only if necessary. but always answer in a very nice and polite way. You dont need to keep all the information from the prompt, often its more than really needed.
    2. If the query asks for **a list (e.g., languages, genres, actors)**, return a **bullet-point list**.
    3. If the query asks for **a fact (e.g., a release year, director name, or language)**, return just the fact with minimal extra information.
    4. If no relevant data is available, **say so explicitly** rather than guessing.
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

    # Construct a **direct** prompt
    prompt = f"""
    User Query: "{query}"

    Available Movie Data:
    {movie_details}

    Graph Relationships:
    {graph_paths}

    Answer the user's question concisely and directly using the provided data.
    If the information is missing, say "I don't have that information."
    """

    response = ollama.chat(
        model='mistral',
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']

def keep_relevant_data_graph(response, query):
    """Keep only relevant data for graph visualization. For this create a prompt with the graph data."""
    movie_details = "\n".join([
        f"""{i+1}. *{m['title']}*
        • Year: {m.get('year', 'N/A')}
        • Plot: {m.get('plot', 'N/A')}
        • Languages: {', '.join(m.get('languages', [])) or 'N/A'}
        • Countries: {', '.join(m.get('countries', [])) or 'N/A'}
        • Genres: {', '.join(m.get('genres', []))}
        • Directed by: {', '.join(m.get('directors', []))}
        """ for i, m in enumerate(response.get("movies", []))
    ])

    graph_paths = build_graph_paths(response["movies"])

    # Construct a **direct** prompt
    prompt = f"""
    User Query: "{query}"

    Available Movie Data:
    {movie_details}

    Graph Relationships:
    {graph_paths}

    You are a graph visualization AI assistant and part of a GraphRAG application.
    I want to visualize the graph relationships between the movies, actors and directors. Please only keep the relevant data for visualization for the users query.
    Please take the same json structure as the input and remove all the data that is not needed for the graph visualization and return it.

    The structure should be like this:
    {{
        "movies": [
            {{
                "title": "Movie Title",
                "actors": ["Actor 1", "Actor 2"],
                "directors": ["Director 1", "Director 2"]
            }}
        ]
    }}

    Thank you!
    """

    system_msg = """
    You are a graph visualization AI assistant and part of a GraphRAG application.
    Your job is to keep only the relevant data for visualization for the user's query." \
    """

    response = ollama.chat(
        model='mistral',
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ]
    )

    try:
        response_json = json.loads(response['message']['content'])
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return "There was an error processing the response."

    return response_json
