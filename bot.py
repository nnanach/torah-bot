from telegram.ext import Dispatcher, MessageHandler, Filters
from app.router import route_message

def handle_message(update, context):
    if update.message is None:
        return

    text = update.message.text or ""
    user_id = update.effective_user.id

    reply = route_message(text, user_id)

    update.message.reply_text(reply)

def build_dispatcher(bot):
    dp = Dispatcher(bot, None, use_context=True)

    dp.add_handler(
        MessageHandler(Filters.text, handle_message)
    )

    return dp
