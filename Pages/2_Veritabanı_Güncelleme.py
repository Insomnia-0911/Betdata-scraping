import sys
import os
import json
import streamlit as st

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from core.driver import SafeDriver
from core.matches import get_match_urls
from core.match_detail import get_match_detail
from core.stats import get_match_stats
from core.odds import get_odds
from core.db import insert_match_full, get_existing_match_ids

DB_PATH = "Database/Betting_Database.db"
DICT_PATH = "Database/Countries_Leagues_Dictionary.json"

st.set_page_config(layout="wide")
st.title("Veritabanı Güncelle")

with open(DICT_PATH, "r", encoding="utf-8") as f:
    countries_leagues = json.load(f)

selected_country = st.selectbox("Ülke", sorted(countries_leagues.keys()))
selected_league = st.selectbox("Lig", sorted(countries_leagues[selected_country]))

current_year = 2025
seasons = [f"{y}/{y+1}" for y in range(2015, current_year + 1)]
selected_season = st.selectbox("Sezon", seasons, index=len(seasons)-1)

if st.button("Başlat"):
    driver = SafeDriver(headless=True)

    existing_ids = get_existing_match_ids(DB_PATH, selected_season)

    match_urls = get_match_urls(
    driver,
    selected_country,
    selected_league,
    selected_season
    )


    progress = st.progress(0)
    total = len(match_urls)
    for i, mid in enumerate(match_urls, start=1):
        data = {}

        data.update(
            get_match_detail(
                driver,
                mid,
                selected_country,
                selected_league,
                selected_season
            )
        )

        data.update(get_match_stats(driver))

        odds = get_odds(driver, mid)

        # 🔥 DEBUG
        print("MATCH:", mid, "ODDS:", odds)
        st.write(mid, odds)

        data.update(odds)

        insert_match_full(DB_PATH, data)

        progress.progress(i / total)

    driver.quit()
    st.success(f"Bitti – {total} maç işlendi")
