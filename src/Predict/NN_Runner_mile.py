import numpy as np
from colorama import init, deinit
from tensorflow.keras.models import load_model
from src.Utils import Expected_Value

init()
model = load_model('Models/NN_Models/Trained-Model-ML')

def nn_runner(data, games, home_team_odds, away_team_odds):
    ml_predictions_array = []

    for row in data:
        ml_predictions_array.append(model.predict(np.array([row])))

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
