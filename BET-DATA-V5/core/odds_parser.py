from core.odds_schema import ODDS_SCHEMA

def build_odds_dict(parsed_markets: dict) -> dict:
    result = {}

    for market, values in parsed_markets.items():
        if market not in ODDS_SCHEMA:
            continue

        for key, odds in values.items():
            schema = ODDS_SCHEMA[market].get(key)
            if not schema:
                continue

            if len(schema) == 2:
                result[schema[0]] = odds[0]
                result[schema[1]] = odds[1]

            elif len(schema) == 4:
                result[schema[0]] = odds[0][0]
                result[schema[1]] = odds[0][1]
                result[schema[2]] = odds[1][0]
                result[schema[3]] = odds[1][1]

    return result
