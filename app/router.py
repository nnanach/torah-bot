from app.chat import chat_reply
from app.jokes import maybe_joke
from app.trades import handle_trade
from app.stats import handle_stats
from app.search import search


def route_message(text: str, user_id: int):
    t = text.lower().strip()

    # --- TRADE COMMANDS ---
    if t.startswith("/trade"):
        return handle_trade(text, user_id)

    if t.startswith("/stats"):
        return handle_stats(user_id)

    # --- JOKES ---
    if "joke" in t:
        return maybe_joke()

    # --- TORAH SEARCH (your core feature) ---
    if "torah" in t or "parsha" in t:
        results = search(text)
        return format_search(results)

    # --- DEFAULT CHAT ---
    return chat_reply(text)


def format_search(results):
    if not results:
        return "No matches found."

    out = []
    for r in results:
        out.append(f"📖 {r['source_path']}\n\n{r['text'][:400]}")
    return "\n\n---\n\n".join(out)
