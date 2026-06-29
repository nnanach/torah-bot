import random

def chat_reply(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Yo. I’m alive."

    if "how are you" in text:
        return "Running clean. No issues."

    if "what are you" in text:
        return "A routing bot with memory potential."

    return random.choice([
        "I didn’t fully catch that.",
        "Try /trade, /stats, or ask about Torah.",
        "Say 'joke' if you want chaos."
    ])
