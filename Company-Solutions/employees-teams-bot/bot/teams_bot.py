from botbuilder.core import ActivityHandler, TurnContext
import os
import requests
from dotenv import load_dotenv

load_dotenv("config/.env")
GRAPH_RAG_API_URL = os.getenv("GRAPH_RAG_API_URL")

class GraphRAGBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        user_message = turn_context.activity.text
        try:
            response = requests.get(
                f"{GRAPH_RAG_API_URL}/ask", 
                params={"query": user_message}
            )
            data = response.json()
            reply = data.get("answer", "Hmm, I couldn't find anything relevant.")
        except Exception:
            reply = "❌ Failed to reach the assistant. Please try again later."
        
        await turn_context.send_activity(reply)
