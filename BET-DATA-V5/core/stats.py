# core/stats.py

from selenium.webdriver.common.by import By
import time


def get_match_stats(driver) -> dict:
    stats = {
        "corner_kicks": None
    }

    try:
        stats_tab = driver.driver.find_element(By.XPATH, "//a[contains(@href,'match-statistics')]")
        stats_tab.click()
        time.sleep(1)

        rows = driver.driver.find_elements(By.CLASS_NAME, "stat__row")
        for row in rows:
            name = row.find_element(By.CLASS_NAME, "stat__categoryName").text.lower()
            if "corner" in name:
                values = row.find_elements(By.CLASS_NAME, "stat__value")
                stats["corner_kicks"] = int(values[0].text) + int(values[1].text)
                break
    except:
        pass

    return stats
