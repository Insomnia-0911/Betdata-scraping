# core/odds_parsers/odds_odd_even.py

from selenium.webdriver.common.by import By
import time


def get_odd_even_odds(driver) -> dict:
    data = {}

    try:
        driver.driver.find_element(
            By.XPATH, "//a[contains(@href,'odd-even')]"
        ).click()
        time.sleep(1)
    except:
        return data

    rows = driver.driver.find_elements(By.CLASS_NAME, "ui-table__row")

    for row in rows:
        try:
            title = row.find_element(By.CLASS_NAME, "ui-table__title").text.lower()
            odds = row.find_elements(By.CLASS_NAME, "oddsCell__odd")

            if len(odds) < 2:
                continue

            odd = odds[0].text
            even = odds[1].text

            # SADECE FULL TIME (legacy ile birebir)
            if "full time" in title or title == "":
                data["odd_open"] = odd
                data["even_open"] = even

        except:
            continue

    return data
