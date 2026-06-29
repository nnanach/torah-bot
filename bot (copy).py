import os
import logging
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, Filters

from search import search

# ---------------- CONFIG ----------------
TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 8080))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

app = Flask(__name__)

# ---------------- LOGIC ----------------
def handle_message(update, context):
    user_text = update.message.text

    results = search(user_text)

    if not results:
        update.message.reply_text("No Torah matches found.")
        return

    reply = []

    for r in results:
        reply.append(
            f"📖 {r['source_path']}\n\n{r['text'][:400]}"
        )

    update.message.reply_text("\n\n---\n\n".join(reply))


# ---------------- TELEGRAM DISPATCHER ----------------
dispatcher = Dispatcher(bot, None, workers=4, use_context=True)
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


# ---------------- WEBHOOK ENDPOINT ----------------
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"


# ---------------- HEALTH CHECK ----------------
@app.route("/", methods=["GET"])
def index():
    return "Torah bot is alive"


# ---------------- MAIN ----------------
def main():
    # Set webhook
    url = os.getenv("WEBHOOK_URL")  # set this in Railway
    if url:
        bot.set_webhook(f"{url}/{TOKEN}")

    app.run(host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
