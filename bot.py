import os
import logging
from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(level=logging.INFO)
print("BOT FILE LOADED")

TOKEN = os.getenv("BOT_TOKEN")
print("TOKEN LOADED:", bool(TOKEN))

def handle_message(update, context):
    print("MESSAGE RECEIVED:", update.message.text)
    update.message.reply_text("alive: " + update.message.text)

def main():
    if not TOKEN:
        print("NO TOKEN FOUND")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("STARTING POLLING")
    updater.start_polling(drop_pending_updates=True)

    updater.idle()

if __name__ == "__main__":
    main()
