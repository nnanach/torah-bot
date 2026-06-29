def handle_trade(text, user_id):
    try:
        parts = text.split()
        _, symbol, direction, entry, exit_, qty = parts

        return (
            f"Trade logged:\n"
            f"{symbol} {direction}\n"
            f"Entry: {entry} Exit: {exit_}\n"
            f"Qty: {qty}"
        )

    except:
        return "Format: /trade TSLA CALL 250 260 1"
