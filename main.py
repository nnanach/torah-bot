from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher

from bot import build_dispatcher
import os

app = Flask(__name__)

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)

dispatcher = build_dispatcher(bot)

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
