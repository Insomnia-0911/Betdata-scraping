# core/odds_parsers/odds_btts.py

from selenium.webdriver.common.by import By
import time


def get_btts_odds(driver) -> dict:
    """
    Both Teams To Score odds
    First Half + Full Time
    """
    data = {}

    try:
        driver.driver.find_element(
            By.XPATH, "//a[contains(@href,'both-teams-to-score')]"
        ).click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")

    for row in rows:
        try:
            market = row.find_element(By.CLASS_NAME, "ui-table__title").text.strip()
            odds = row.find_elements(By.CLASS_NAME, "oddsCell__odd")

            if len(odds) < 2:
                continue

            yes = odds[0].text
            no = odds[1].text

            # --- FIRST HALF ---
            if "1st Half" in market:
                data["firsthalf_both_teams_to_score_yes_open"] = yes
                data["firsthalf_both_teams_to_score_no_open"] = no

            # --- FULL TIME ---
            else:
                data["both_teams_to_score_yes_open"] = yes
                data["both_teams_to_score_no_open"] = no

        except:
            continue

    return data
