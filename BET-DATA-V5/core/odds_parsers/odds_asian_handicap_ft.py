# core/odds_parsers/odds_asian_handicap_ft.py
from selenium.webdriver.common.by import By
import time

def get_asian_handicap_ft(driver) -> dict:
    data = {}
    try:
        driver.driver.find_element(By.XPATH, "//a[contains(@href,'asian-handicap')]").click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")
    for r in rows:
        try:
            line = r.find_element(By.CLASS_NAME, "ui-table__title").text.replace(" ", "")
            odds = r.find_elements(By.CLASS_NAME, "oddsCell__odd")
            if len(odds) >= 2:
                data[f"fulltime_asian_handicap_{line}_home_open"] = odds[0].text
                data[f"fulltime_asian_handicap_{line}_away_open"] = odds[1].text
        except:
            pass
    return data
