from selenium.webdriver.common.by import By
from datetime import datetime


def get_match_detail(driver, match_id: str, country: str, league: str, season: str) -> dict:
    url = f"https://www.flashscore.co.uk/match/{match_id}/#/match-summary"
    driver.get(url, wait_css="div.duelParticipant")

    data = {
        "match_id": match_id,
        "country": country.upper(),
        "league": league,
        "season": season,
    }

    # --- COUNTRY / LEAGUE OVERWRITE ---
    try:
        breadcrumb = driver.driver.find_element(By.CLASS_NAME, "breadcrumb").text
        parts = [p.strip() for p in breadcrumb.split("/")]

        if len(parts) >= 3:
            data["country"] = parts[1].upper()
            data["league"] = parts[2]
    except:
        pass

    # --- TEAMS ---
    try:
        teams = driver.driver.find_elements(By.CLASS_NAME, "participant__participantName")
        data["home_team_name"] = teams[0].text
        data["away_team_name"] = teams[1].text
    except:
        pass

    # --- SCORE ---
    try:
        score = driver.driver.find_element(By.CLASS_NAME, "detailScore__wrapper").text
        data["match_time_score"] = score
        data["match_result_score"] = score
    except:
        pass

    # --- DATE ---
    try:
        time_el = driver.driver.find_element(By.CLASS_NAME, "duelParticipant__startTime")
        dt = datetime.strptime(time_el.text, "%d.%m.%Y %H:%M")
        data["date"] = dt.date().isoformat()
        data["hour"] = dt.strftime("%H:%M")
        data["day"] = dt.day
        data["month"] = dt.month
        data["year"] = dt.year
        data["weekday"] = dt.weekday()
    except:
        pass

    return data
