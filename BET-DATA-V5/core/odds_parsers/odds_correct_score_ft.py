# core/odds_parsers/odds_correct_score_ft.py
from selenium.webdriver.common.by import By
import time

SCORES = [
    "0:0","1:0","2:0","2:1","3:0","3:1","3:2","4:0","4:1","4:2","4:3",
    "1:1","2:2","3:3","4:4",
    "0:1","0:2","1:2","0:3","1:3","2:3","0:4","1:4","2:4","3:4"
]

def get_correct_score_ft(driver) -> dict:
    data = {}
    try:
        driver.driver.find_element(By.XPATH, "//a[contains(@href,'correct-score')]").click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")
    for r in rows:
        try:
            score = r.find_element(By.CLASS_NAME, "ui-table__title").text
            if score not in SCORES:
                continue
            odds = r.find_elements(By.CLASS_NAME, "oddsCell__odd")
            data[f"match_time_{score.replace(':','_')}_open"] = odds[0].text if odds else None
        except:
            pass
    return data
