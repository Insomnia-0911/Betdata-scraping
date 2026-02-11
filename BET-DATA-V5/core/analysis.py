# core/analysis.py

import pandas as pd
import sqlite3


def load_matches(db_path: str) -> pd.DataFrame:
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM match_bet_data", conn)
    conn.close()
    return df


def apply_filters(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    for key, value in filters.items():
        if value is False:
            continue
        if key in df.columns:
            df = df[df[key] == value]
    return df
