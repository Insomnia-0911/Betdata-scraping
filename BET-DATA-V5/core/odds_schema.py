# core/odds_schema.py

ODDS_SCHEMA = {

    # ==================================================
    # FULL TIME RESULT
    # ==================================================
    "fulltime_result": {
        "1": ("fulltime_home_open", "fulltime_home_close"),
        "X": ("fulltime_tie_open", "fulltime_tie_close"),
        "2": ("fulltime_away_open", "fulltime_away_close"),
    },

    # ==================================================
    # FIRST HALF RESULT
    # ==================================================
    "firsthalf_result": {
        "1": ("firsthalf_home_open", "firsthalf_home_close"),
        "X": ("firsthalf_tie_open", "firsthalf_tie_close"),
        "2": ("firsthalf_away_open", "firsthalf_away_close"),
    },

    # ==================================================
    # SECOND HALF RESULT
    # ==================================================
    "secondhalf_result": {
        "1": ("secondhalf_home_open", "secondhalf_home_close"),
        "X": ("secondhalf_tie_open", "secondhalf_tie_close"),
        "2": ("secondhalf_away_open", "secondhalf_away_close"),
    },

    # ==================================================
    # HT / FT
    # ==================================================
    "ht_ft": {
        "1/1": ("home_home_open", "home_home_close"),
        "1/X": ("home_tie_open", "home_tie_close"),
        "1/2": ("home_away_open", "home_away_close"),
        "X/1": ("tie_home_open", "tie_home_close"),
        "X/X": ("tie_tie_open", "tie_tie_close"),
        "X/2": ("tie_away_open", "tie_away_close"),
        "2/1": ("away_home_open", "away_home_close"),
        "2/X": ("away_tie_open", "away_tie_close"),
        "2/2": ("away_away_open", "away_away_close"),
    },

    # ==================================================
    # BOTH TEAMS TO SCORE
    # ==================================================
    "btts": {
        "YES": ("both_teams_to_score_yes_open", "both_teams_to_score_yes_close"),
        "NO": ("both_teams_to_score_no_open", "both_teams_to_score_no_close"),
    },

    # ==================================================
    # OVER / UNDER (FULL TIME)
    # ==================================================
    "over_under_fulltime": {
        "0.5": ("match_time_over_0_5_open", "match_time_over_0_5_close",
                "match_time_under_0_5_open", "match_time_under_0_5_close"),
        "1.5": ("match_time_over_1_5_open", "match_time_over_1_5_close",
                "match_time_under_1_5_open", "match_time_under_1_5_close"),
        "2.5": ("match_time_over_2_5_open", "match_time_over_2_5_close",
                "match_time_under_2_5_open", "match_time_under_2_5_close"),
        "3.5": ("match_time_over_3_5_open", "match_time_over_3_5_close",
                "match_time_under_3_5_open", "match_time_under_3_5_close"),
    },

    # ==================================================
    # OVER / UNDER (FIRST HALF)
    # ==================================================
    "over_under_firsthalf": {
        "0.5": ("first_half_over_0_5_open", "first_half_over_0_5_close",
                "first_half_under_0_5_open", "first_half_under_0_5_close"),
        "1.5": ("first_half_over_1_5_open", "first_half_over_1_5_close",
                "first_half_under_1_5_open", "first_half_under_1_5_close"),
    },

    # ==================================================
    # CORRECT SCORE – FIRST HALF
    # ==================================================
    "correct_score_firsthalf": {
        "0:0": ("first_half_0_0_open", "first_half_0_0_close"),
        "1:0": ("first_half_1_0_open", "first_half_1_0_close"),
        "2:0": ("first_half_2_0_open", "first_half_2_0_close"),
        "2:1": ("first_half_2_1_open", "first_half_2_1_close"),
        "1:1": ("first_half_1_1_open", "first_half_1_1_close"),
        "3:0": ("first_half_3_0_open", "first_half_3_0_close"),
        "3:1": ("first_half_3_1_open", "first_half_3_1_close"),
        "3:2": ("first_half_3_2_open", "first_half_3_2_close"),
        "4:0": ("first_half_4_0_open", "first_half_4_0_close"),
        "4:1": ("first_half_4_1_open", "first_half_4_1_close"),
        "4:2": ("first_half_4_2_open", "first_half_4_2_close"),
        "4:3": ("first_half_4_3_open", "first_half_4_3_close"),
    },

    # ==================================================
    # CORRECT SCORE – FULL TIME
    # ==================================================
    "correct_score_fulltime": {
        "0:0": ("match_time_0_0_open", "match_time_0_0_close"),
        "1:0": ("match_time_1_0_open", "match_time_1_0_close"),
        "2:0": ("match_time_2_0_open", "match_time_2_0_close"),
        "2:1": ("match_time_2_1_open", "match_time_2_1_close"),
        "1:1": ("match_time_1_1_open", "match_time_1_1_close"),
        "3:0": ("match_time_3_0_open", "match_time_3_0_close"),
        "3:1": ("match_time_3_1_open", "match_time_3_1_close"),
        "3:2": ("match_time_3_2_open", "match_time_3_2_close"),
        "4:0": ("match_time_4_0_open", "match_time_4_0_close"),
        "4:1": ("match_time_4_1_open", "match_time_4_1_close"),
        "4:2": ("match_time_4_2_open", "match_time_4_2_close"),
        "4:3": ("match_time_4_3_open", "match_time_4_3_close"),
    },

    # ==================================================
    # ASIAN HANDICAP (GENERIC)
    # ==================================================
    "asian_handicap": {
        "-2": ("fulltime_asian_handicap_neg2_home_open",
               "fulltime_asian_handicap_neg2_home_close",
               "fulltime_asian_handicap_neg2_away_open",
               "fulltime_asian_handicap_neg2_away_close"),
        "-1.5": ("fulltime_asian_handicap_neg1_5_home_open",
                 "fulltime_asian_handicap_neg1_5_home_close",
                 "fulltime_asian_handicap_neg1_5_away_open",
                 "fulltime_asian_handicap_neg1_5_away_close"),
        "-1": ("fulltime_asian_handicap_neg_1_home_open",
               "fulltime_asian_handicap_neg_1_home_close",
               "fulltime_asian_handicap_neg_1_away_open",
               "fulltime_asian_handicap_neg_1_away_close"),
        "-0.5": ("fulltime_asian_handicap_neg_0_5_home_open",
                 "fulltime_asian_handicap_neg_0_5_home_close",
                 "fulltime_asian_handicap_neg_0_5_away_open",
                 "fulltime_asian_handicap_neg_0_5_away_close"),
        "+0.5": ("fulltime_asian_handicap_pos_0_5_home_open",
                 "fulltime_asian_handicap_pos_0_5_home_close",
                 "fulltime_asian_handicap_pos_0_5_away_open",
                 "fulltime_asian_handicap_pos_0_5_away_close"),
        "+1": ("fulltime_asian_handicap_pos_1_home_open",
               "fulltime_asian_handicap_pos_1_home_close",
               "fulltime_asian_handicap_pos_1_away_open",
               "fulltime_asian_handicap_pos_1_away_close"),
    }
}
