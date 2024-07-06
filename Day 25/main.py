from screen_setup import Screen
import pandas as pd

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
guess_state = []
missing_state = []

def get_x(word):
    x_loc = data[data['state'] == word]['x'].iloc[0]
    return x_loc

def get_y(word):
    y_loc = data[data['state'] == word]['y'].iloc[0]
    return y_loc

screen = Screen()
play_game = True

while play_game:
    answer = screen.ask_question()
    if answer in states:
        screen.number += 1
        guess_state.append(answer)
        x_pos = get_x(answer)
        y_pos = get_y(answer)
        screen.create_label(x_pos, y_pos, answer)
    else:
        play_game = False
        screen.total_score()
        for state in states:
            if state not in guess_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("to_review.csv")
        
screen.run()
