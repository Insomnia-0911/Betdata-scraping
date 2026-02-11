# core/odds_parsers/odds_1x2.py
from selenium.webdriver.common.by import By
import time

def get_1x2_odds(driver, match_id):
    url = f"https://www.flashscore.co.uk/match/{match_id}/#/odds-comparison/1x2"
    driver.get(url)

    time.sleep(2)  # 🔴 ZORUNLU

    data = {}

    rows = driver.driver.find_elements(By.CSS_SELECTOR, "div.ui-table__row")

    if len(rows) < 1:
        return data  # boş döner ama artık GERÇEKTEN boş

    # OPEN (ilk bookmaker)
    open_odds = rows[0].find_elements(By.CSS_SELECTOR, "span.oddsCell__odd")
    if len(open_odds) >= 3:
        data["fulltime_home_open"] = open_odds[0].text
        data["fulltime_tie_open"] = open_odds[1].text
        data["fulltime_away_open"] = open_odds[2].text

    # CLOSE (son bookmaker)
    close_odds = rows[-1].find_elements(By.CSS_SELECTOR, "span.oddsCell__odd")
    if len(close_odds) >= 3:
        data["fulltime_home_close"] = close_odds[0].text
        data["fulltime_tie_close"] = close_odds[1].text
        data["fulltime_away_close"] = close_odds[2].text

    return data
