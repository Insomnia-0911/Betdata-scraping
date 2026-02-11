# Pages/3_Bülten_Güncelleme.py
import sys, os
import streamlit as st
from datetime import date, timedelta

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from core.driver import SafeDriver
from core.bulletin import get_bulletin_match_ids
from core.match_detail import get_match_detail
from core.odds import get_full_odds_tuple
from core.db import insert_match_full

DB_PATH = "Database/Betting_Database.db"

st.title("Bülten Güncelle – FULL ANALİST MODU")

if st.button("Bugünkü Tüm Maçları Çek (FULL)"):
    driver = SafeDriver(headless=True)
    target_date = date.today()

    match_ids = get_bulletin_match_ids(driver, target_date)

    ok, fail = 0, 0

    for mid in match_ids:
        try:
            context = get_match_detail(
                driver,
                mid,
                country="AUTO",
                league="AUTO",
                season="AUTO"
            )

            data_to_insert = get_full_odds_tuple(**context)
            insert_match_full(DB_PATH, data_to_insert)

            ok += 1
        except:
            fail += 1

    driver.quit()
    st.success(f"Bitti | Başarılı: {ok} | Hatalı: {fail}")
