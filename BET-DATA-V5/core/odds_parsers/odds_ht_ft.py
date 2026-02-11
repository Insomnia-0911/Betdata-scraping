# core/odds_parsers/odds_ht_ft.py
from selenium.webdriver.common.by import By
import time

def get_ht_ft_odds(driver) -> dict:
    data = {}
    try:
        driver.driver.find_element(By.XPATH, "//a[contains(@href,'ht-ft')]").click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")
    for r in rows:
        try:
            key = r.find_element(By.CLASS_NAME, "ui-table__title").text.replace("/", "_")
            odds = r.find_elements(By.CLASS_NAME, "oddsCell__odd")
            data[f"{key}_open"] = odds[0].text if odds else None
        except:
            pass
    return data
