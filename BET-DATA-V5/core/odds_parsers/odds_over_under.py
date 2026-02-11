# core/odds_parsers/odds_over_under.py

from selenium.webdriver.common.by import By
import time


def get_over_under_odds(driver) -> dict:
    data = {}

    try:
        driver.driver.find_element(
            By.XPATH, "//a[contains(@href,'over-under')]"
        ).click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")

    for row in rows:
        try:
            title = row.find_element(By.CLASS_NAME, "ui-table__title").text.strip()
            odds = row.find_elements(By.CLASS_NAME, "oddsCell__odd")

            if len(odds) < 2:
                continue

            over = odds[0].text
            under = odds[1].text

            # -------- FIRST HALF --------
            if "1st Half" in title:
                if "0.5" in title:
                    data["first_half_over_0_5_open"] = over
                    data["first_half_under_0_5_open"] = under
                elif "1.5" in title:
                    data["first_half_over_1_5_open"] = over
                    data["first_half_under_1_5_open"] = under

            # -------- FULL TIME --------
            else:
                if "0.5" in title:
                    data["match_time_over_0_5_open"] = over
                    data["match_time_under_0_5_open"] = under
                elif "1.5" in title:
                    data["match_time_over_1_5_open"] = over
                    data["match_time_under_1_5_open"] = under
                elif "2.5" in title:
                    data["match_time_over_2_5_open"] = over
                    data["match_time_under_2_5_open"] = under
                elif "3.5" in title:
                    data["match_time_over_3_5_open"] = over
                    data["match_time_under_3_5_open"] = under

        except:
            continue

    return data
