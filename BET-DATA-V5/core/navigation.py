MAIN_URL = "https://www.flashscore.co.uk"


def normalize_country(country: str) -> str:
    return country.lower().replace(" & ", "-").replace(" ", "-")


def normalize_league(league: str) -> str:
    return (
        league.lower()
        .replace(" ", "-")
        .replace(".", "")
        .replace("'", "-")
    )


def build_results_urls(country: str, league: str, season: str) -> list[str]:
    season_start, season_end = season.split("/")

    urls = []

    urls.append(
        f"{MAIN_URL}/football/"
        f"{normalize_country(country)}/"
        f"{normalize_league(league)}-"
        f"{season_start}-{season_end}/results/"
    )

    urls.append(
        f"{MAIN_URL}/football/"
        f"{normalize_country(country)}/"
        f"{normalize_league(league)}-"
        f"{season_start}/results/"
    )

    return urls
