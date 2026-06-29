import os
from telegram.ext import Updater, MessageHandler, Filters
from search import search

TOKEN = os.getenv("BOT_TOKEN")

def handle_message(update, context):
    text = update.message.text
    results = search(text)

    if not results:
        update.message.reply_text("No Torah matches found.")
        return

    reply = [
        f"📖 {r['source_path']}\n\n{r['text'][:400]}"
        for r in results
    ]

    update.message.reply_text("\n\n---\n\n".join(reply))


def main():
    updater = Updater(TOKEN, use_context=True)

    # 🔥 critical reset against stale sessions
    updater.bot.delete_webhook(drop_pending_updates=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling(drop_pending_updates=True)
    updater.idle()


if __name__ == "__main__":
    main()
