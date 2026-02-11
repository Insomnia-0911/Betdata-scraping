# core/odds_parsers/odds_double_chance.py

from selenium.webdriver.common.by import By
import time


def get_double_chance_odds(driver) -> dict:
    data = {}

    try:
        driver.driver.find_element(
            By.XPATH, "//a[contains(@href,'double-chance')]"
        ).click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")

    for row in rows:
        try:
            title = row.find_element(By.CLASS_NAME, "ui-table__title").text.strip()
            odds = row.find_elements(By.CLASS_NAME, "oddsCell__odd")

            if len(odds) < 3:
                continue

            home_tie = odds[0].text
            home_away = odds[1].text
            tie_away = odds[2].text

            # --- FIRST HALF ---
            if "1st Half" in title:
                data["first_half_home_and_tie_open"] = home_tie
                data["first_half_home_and_away_open"] = home_away
                data["first_half_tie_and_away_open"] = tie_away

            # --- FULL TIME ---
            else:
                data["match_time_home_and_tie_open"] = home_tie
                data["match_time_home_and_away_open"] = home_away
                data["match_time_tie_and_away_open"] = tie_away

        except:
            continue

    return data
