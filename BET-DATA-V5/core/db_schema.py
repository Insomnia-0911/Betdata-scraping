# core/db_schema.py
import sqlite3

def get_table_columns(db_path: str, table_name: str) -> list[str]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]

    conn.close()
    return columns
