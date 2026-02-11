# core/db.py
import sqlite3


def insert_match_full(db_path: str, data: dict):
    """
    match_bet_data tablosuna:
    - match_id yoksa INSERT
    - varsa SADECE gelen kolonları UPDATE eder
    """
    if "match_id" not in data:
        raise ValueError("match_id olmadan DB insert yapılamaz")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # DB kolonlarını oku
    cursor.execute("PRAGMA table_info(match_bet_data)")
    table_columns = [row[1] for row in cursor.fetchall()]

    # DB'de olmayan kolonları at
    clean_data = {k: data[k] for k in data if k in table_columns}

    if not clean_data:
        conn.close()
        raise ValueError("DB ile eşleşen hiçbir kolon bulunamadı")

    columns = list(clean_data.keys())
    values = [clean_data[c] for c in columns]

    insert_cols = ", ".join(columns)
    insert_vals = ", ".join("?" for _ in columns)

    # UPDATE kısmı (match_id hariç)
    update_clause = ", ".join(
        f"{col}=excluded.{col}"
        for col in columns
        if col != "match_id"
    )

    query = f"""
        INSERT INTO match_bet_data ({insert_cols})
        VALUES ({insert_vals})
        ON CONFLICT(match_id) DO UPDATE SET
        {update_clause}
    """

    cursor.execute(query, values)
    conn.commit()
    conn.close()


def get_existing_match_ids(db_path, season=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if season:
        cursor.execute(
            "SELECT match_id FROM match_bet_data WHERE season = ?",
            (season,)
        )
    else:
        cursor.execute("SELECT match_id FROM match_bet_data")

    rows = cursor.fetchall()
    conn.close()

    return [r[0] for r in rows]
