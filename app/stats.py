from app.db import get_conn

def handle_stats(user_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT symbol, entry, exit, qty
        FROM trades
        WHERE user_id = ?
    """, (user_id,))

    rows = cur.fetchall()

    conn.close()

    if not rows:
        return "No trades logged."

    total = len(rows)
    wins = 0
    pnl = 0

    for symbol, entry, exit_, qty in rows:
        trade_pnl = (exit_ - entry) * qty

        pnl += trade_pnl

        if trade_pnl > 0:
            wins += 1

    win_rate = wins / total

    return (
        f"Trades: {total}\n"
        f"Wins: {wins}\n"
        f"Win Rate: {win_rate:.1%}\n"
        f"PnL: {pnl:.2f}"
    )
