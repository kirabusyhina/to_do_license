import sqlite3
import hashlib
from datetime import datetime, timedelta

DB_PATH = "licenses.db"

def hash_key(key: str) -> str:
    return hashlib.sha256(key.strip().encode("utf-8")).hexdigest()

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS licenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        license_hash TEXT UNIQUE NOT NULL,
        user_email TEXT NOT NULL,
        is_active INTEGER NOT NULL DEFAULT 1,
        expires_at TEXT NOT NULL
    )
    """)

    # Тестовые данные
    # Реальный ключ, которые выдаются "покупателю":
    test_license_key = "kira-2026-demo-1024"
    test_user_email = "kira@gmail.com"

    expires = (datetime.utcnow() + timedelta(days=30)).isoformat()

    try:
        cur.execute("""
            INSERT INTO licenses (license_hash, user_email, is_active, expires_at)
            VALUES (?, ?, 1, ?)
        """, (hash_key(test_license_key), test_user_email, expires))
        conn.commit()
        print("OK: License inserted.")
        print("TEST LICENSE KEY:", test_license_key)
        print("USER EMAIL:", test_user_email)
        print("EXPIRES:", expires)
    except sqlite3.IntegrityError:
        print("License already exists. No changes made.")

    conn.close()

if __name__ == "__main__":
    main()
