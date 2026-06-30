from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher
from app.db import init_db
from bot import build_dispatcher
import os

print("TOKEN PREFIX:", TOKEN[:10] if TOKEN else "NONE")

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)

dispatcher = build_dispatcher(bot)

init_db()   # ← ALWAYS runs on import (safe, idempotent)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "alive"

def set_webhook():
    url = os.getenv("WEBHOOK_URL")
    bot.set_webhook(f"{url}/webhook")

if __name__ == "__main__":
    set_webhook()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
