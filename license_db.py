import sqlite3
import hashlib
from datetime import datetime

DB_PATH = "licenses.db"

def hash_key(key: str) -> str:
    return hashlib.sha256(key.strip().encode("utf-8")).hexdigest()

def validate_license(license_key: str, user_email: str) -> tuple[bool, str]:
    """
    Returns (is_valid, message).
    """
    if not license_key.strip() or not user_email.strip():
        return False, "License key and email are required."

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT user_email, is_active, expires_at
        FROM licenses
        WHERE license_hash = ?
    """, (hash_key(license_key),))

    row = cur.fetchone()
    conn.close()

    if not row:
        return False, "Invalid license key."

    db_email, is_active, expires_at = row

    if str(db_email).strip().lower() != user_email.strip().lower():
        return False, "License key does not belong to this user."

    if int(is_active) != 1:
        return False, "License is not active."

    try:
        exp_dt = datetime.fromisoformat(expires_at)
    except ValueError:
        return False, "License data corrupted (invalid expiry format)."

    if datetime.utcnow() > exp_dt:
        return False, "License has expired."

    return True, "License validated."
