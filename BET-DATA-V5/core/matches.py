# core/matches.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from core.navigation import build_results_urls


def load_all_matches(driver, max_click=200):
    click_count = 0

    while click_count < max_click:
        try:
            show_more = driver.driver.find_element(
                By.XPATH,
                "//a[contains(@class,'event__more') and contains(@class,'event__more--static')]"
            )
            driver.driver.execute_script(
                "arguments[0].scrollIntoView(true);", show_more
            )
            show_more.click()
            click_count += 1
            time.sleep(0.8)
        except:
            rounds = driver.driver.find_elements(
                By.CLASS_NAME, "event__round--static"
            )
            if not rounds:
                break
            click_count += 1


def get_match_ids(
    driver,
    country: str,
    league: str,
    season: str,
    existing_ids: list[str]
) -> list[str]:
    urls = build_results_urls(country, league, season)

    for url in urls:
        try:
            driver.get(url, wait_css="div.event__match")
            time.sleep(2)

            # Sayfa hata kontrolü
            error_elements = driver.driver.find_elements(By.CSS_SELECTOR, "main > p")
            if error_elements and "Error" in error_elements[0].text:
                raise Exception("Page error")

            no_match = driver.driver.find_elements(By.CLASS_NAME, "nmf__title")
            if no_match:
                raise Exception("No match found")
            load_all_matches(driver)
            match_elements = driver.driver.find_elements(
                By.XPATH,
                "//div[contains(@class,'event__match') and contains(@class,'event__match--static')]"
            )

            match_ids = []
            for el in match_elements:
                mid = el.get_attribute("id")
                if mid:
                    match_ids.append(mid.split("_")[-1])

            match_ids = list(reversed(match_ids))
            filtered = [m for m in match_ids if m not in existing_ids]

            return filtered

        except:
            continue
    

    return []
def get_match_urls(
    driver,
    country: str,
    league: str,
    season: str
) -> list[str]:
    urls = build_results_urls(country, league, season)
    match_urls = []

    for url in urls:
        try:
            driver.get(url, wait_css="div.event__match")
            time.sleep(2)

            load_all_matches(driver)

            match_elements = driver.driver.find_elements(
                By.XPATH,
                "//div[contains(@class,'event__match') and contains(@class,'event__match--static')]//a"
            )

            for a in match_elements:
                href = a.get_attribute("href")
                if href and "/match/" in href:
                    match_urls.append(href)

            if match_urls:
                return list(dict.fromkeys(match_urls))

        except:
            continue

    return []

