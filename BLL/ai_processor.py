from openai import OpenAI
import config.settings as settings
from BLL.retrieval import retrieve_context

# Initialize OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_response(query):
    """
    Generates an AI response using OpenAI GPT-4 based on retrieved context.
    Ensures minimal token usage to avoid rate limits.
    """
    related_movies = retrieve_context(query, limit=15)

    knowledge_text = "\n".join([
    f"🎬 {movie.get('movie', 'Unknown Movie')} ({movie.get('year', 'Year Unknown')})\n"
    f"   Actors: {', '.join(movie.get('actors', [])[:3])}\n"
    f"   Director: {', '.join(movie.get('directors', [])[:2])}\n"
    f"   Genres: {', '.join(movie.get('genres', [])[:2])}\n"
    for movie in related_movies
])

    prompt = f"""
    You are a helpful AI assistant. Based on the following knowledge, answer the user's question:

    Knowledge:
    {knowledge_text}

    User Question: {query}

    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert assistant using GraphRAG for knowledge retrieval."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
