import sqlite3

DB = "app.db"

def init_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # USERS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        plan TEXT DEFAULT 'free'
    )
    """)

    # TRADES TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        symbol TEXT,
        direction TEXT,
        entry REAL,
        exit REAL,
        qty REAL,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()
