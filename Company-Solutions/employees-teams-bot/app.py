import os
from fastapi import FastAPI, Request
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    BotFrameworkAdapter,
    TurnContext
)
from botbuilder.schema import Activity
from bot.teams_bot import GraphRAGBot
from dotenv import load_dotenv

load_dotenv("config/.env")

app = FastAPI()
bot = GraphRAGBot()

SETTINGS = BotFrameworkAdapterSettings(
    app_id=os.getenv("MICROSOFT_APP_ID"),
    app_password=os.getenv("MICROSOFT_APP_PASSWORD")
)
ADAPTER = BotFrameworkAdapter(SETTINGS)

@app.post("/api/messages")
async def messages(req: Request):
    body = await req.json()
    activity = Activity().deserialize(body)

    auth_header = req.headers.get("Authorization", "")
    
    async def call_bot(turn_context: TurnContext):
        await bot.on_turn(turn_context)

    return await ADAPTER.process_activity(activity, auth_header, call_bot)
