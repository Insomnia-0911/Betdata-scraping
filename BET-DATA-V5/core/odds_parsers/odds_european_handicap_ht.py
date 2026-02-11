# core/odds_parsers/odds_european_handicap_ht.py
from selenium.webdriver.common.by import By
import time

def get_european_handicap_ht(driver) -> dict:
    data = {}
    try:
        driver.driver.find_element(By.XPATH, "//a[contains(@href,'european-handicap')]").click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")
    for r in rows:
        try:
            line = r.find_element(By.CLASS_NAME, "ui-table__title").text.replace(" ", "")
            odds = r.find_elements(By.CLASS_NAME, "oddsCell__odd")
            if len(odds) == 3:
                data[f"firsthalf_european_handicap_{line}_home_open"] = odds[0].text
                data[f"firsthalf_european_handicap_{line}_tie_open"] = odds[1].text
                data[f"firsthalf_european_handicap_{line}_away_open"] = odds[2].text
        except:
            pass
    return data