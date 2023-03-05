import numpy as np
import xgboost as xgb
from colorama import init, deinit
from src.Utils import Expected_Value


# from src.Utils.Dictionaries import team_index_current
# from src.Utils.tools import get_json_data, to_data_frame, get_todays_games_json, create_todays_games
init()
xgb_ml = xgb.Booster()
xgb_ml.load_model('Models/XGBoost_Models/XGBoost_68.3%_ML-2.json')


def xgb_runner(data, games, home_team_odds, away_team_odds):
    ml_predictions_array = []

    for row in data:
        ml_predictions_array.append(xgb_ml.predict(xgb.DMatrix(np.array([row]))))

    count = 0
    predicted_results = []  # create an empty list to store the predicted results
    for game in games:
        home_team = game[0]
        away_team = game[1]
        winner = int(np.argmax(ml_predictions_array[count]))
        winner_confidence = ml_predictions_array[count]
        ev_home = ev_away = 0
        if home_team_odds[count] and away_team_odds[count]:
            ev_home = float(Expected_Value.expected_value(ml_predictions_array[count][0][1], int(home_team_odds[count])))
            ev_away = float(Expected_Value.expected_value(ml_predictions_array[count][0][0], int(away_team_odds[count])))
        
        predicted_result = {}
        predicted_result['home_team'] = home_team
        predicted_result['away_team'] = away_team
        predicted_result['winner'] = str(winner)
        predicted_result['winner_confidence'] = str(winner_confidence)
        predicted_result['ev_home'] = str(ev_home)
        predicted_result['ev_away'] = str(ev_away)

        predicted_results.append(predicted_result)  # append the predicted result to the list

        count += 1

    deinit()
    return predicted_results
