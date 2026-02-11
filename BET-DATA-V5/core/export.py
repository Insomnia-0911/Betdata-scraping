# core/export.py

import pandas as pd
import sqlite3
from openpyxl import Workbook


def export_to_excel(db_path: str, table: str, output_path: str):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    conn.close()

    df.to_excel(output_path, index=False)
