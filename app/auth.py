from telegram.ext import Dispatcher, MessageHandler, Filters
from app.handlers import handle_message

def build_dispatcher(bot):
    dp = Dispatcher(bot, None, use_context=True)

    dp.add_handler(
        MessageHandler(Filters.text & ~Filters.command, handle_message)
    )

    return dp
