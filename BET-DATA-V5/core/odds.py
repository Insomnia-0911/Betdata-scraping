# core/odds.py

from core.odds_parsers.odds_1x2 import get_1x2_odds
from core.odds_parsers.odds_double_chance import get_double_chance_odds
from core.odds_parsers.odds_over_under import get_over_under_odds
from core.odds_parsers.odds_btts import get_btts_odds
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_odds(driver, match_url):
    base = match_url.split("?")[0]

    odds = {}

    odds.update(get_1x2_odds(driver, base + "#/odds-comparison/1x2-odds/full-time"))
    odds.update(get_over_under_odds(driver, base + "#/odds-comparison/over-under/full-time"))
    odds.update(get_btts_odds(driver, base + "#/odds-comparison/both-teams-to-score/full-time"))
    odds.update(get_double_chance_odds(driver, base + "#/odds-comparison/double-chance/full-time"))

    return odds