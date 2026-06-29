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
    print("HELLO FROM BOT")
    while True:
        pass
        
if __name__ == "__main__":
    main()
