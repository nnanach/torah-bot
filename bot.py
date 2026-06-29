import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("BOT_TOKEN")

def handle_message(update, context):
    update.message.reply_text("alive: " + update.message.text)

def main():
    print("BOT STARTING")

    if not TOKEN:
        print("NO TOKEN")
        return

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling(drop_pending_updates=True)
    updater.idle()

if __name__ == "__main__":
    main()
