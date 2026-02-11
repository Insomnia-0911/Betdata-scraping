# core/bulletin.py
from selenium.webdriver.common.by import By
from datetime import date


def get_bulletin_match_ids(driver, target_date: date) -> list[str]:
    """
    Bugünkü / yarınki TÜM maçların match_id listesini döndürür
    """

    url = "https://www.flashscore.co.uk/football/"
    driver.get(url, wait_css="div.event__match")

    match_elements = driver.driver.find_elements(
        By.XPATH,
        "//div[contains(@class,'event__match')]"
    )

    match_ids = []

    for el in match_elements:
        raw_id = el.get_attribute("id")
        if not raw_id:
            continue

        match_id = raw_id.split("_")[-1]
        match_ids.append(match_id)

    return list(set(match_ids))
