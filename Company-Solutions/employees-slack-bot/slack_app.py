from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import requests

load_dotenv("config/.env")

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
GRAPH_RAG_API_URL = os.getenv("GRAPH_RAG_API_URL")

app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)
fastapi_app = FastAPI()
handler = SlackRequestHandler(app)

@app.event("app_mention")
def handle_mention(event, say):
    user_query = event["text"].split(">", 1)[-1].strip()
    
    try:
        res = requests.get(f"{GRAPH_RAG_API_URL}/ask", params={"query": user_query})
        data = res.json()
        say(data.get("answer", "Sorry, I couldn't understand that."))
    except Exception as e:
        say("❌ Failed to reach the assistant. Please try again later.")

@fastapi_app.post("/slack/events")
async def slack_events(request: Request):
    return await handler.handle(request)
