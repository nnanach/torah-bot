from app.db import get_conn

def handle_trade(text, user_id):
    try:
        _, symbol, direction, entry, exit_, qty = text.split()

        conn = get_conn()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO trades
            (user_id, symbol, direction, entry, exit, qty)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            symbol.upper(),
            direction.upper(),
            float(entry),
            float(exit_),
            float(qty)
        ))

        conn.commit()
        conn.close()

        return (
            f"Saved trade:\n"
            f"{symbol.upper()} {direction.upper()}\n"
            f"Entry: {entry}\n"
            f"Exit: {exit_}\n"
            f"Qty: {qty}"
        )

    except Exception as e:
        return f"Trade error: {e}"
