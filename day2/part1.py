import re
from typing import List


# 48 minutes


# I have used the term game round because it was becoming to confusing and set is a reserved word
def get_nb_for_each_color(game_rounds: List[str]):
    name_color_nb_dict: {str, int} = {}
    for round in game_rounds:
        # split each round
        nb_and_name_colors: List[str] = round.split(',')
        for nb_and_name_color in nb_and_name_colors:
            # regex to get the values
            nb_colors: int = int(re.search(r'\d+', nb_and_name_color).group())
            name_colors: str = re.search(r'[a-zA-z]+', nb_and_name_color).group()
            # check if is present in the dict, otherwise check if the value is higher than the one in there
            if name_color_nb_dict.get(name_colors) is None or name_color_nb_dict[name_colors] < nb_colors:
                name_color_nb_dict[name_colors] = nb_colors
    return name_color_nb_dict


sum_no_game: int = 0
nb_red: int = 12
nb_green: int = 13
nb_blue: int = 14

color_max_val_dict: {str, int} = {
    'red': nb_red,
    'green': nb_green,
    'blue': nb_blue
}

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(':')
        # get no of the game
        no_game_match: re.match = re.search(r'\d+', line[0])
        no_game: int = int(no_game_match.group())

        # get the results from the game
        rounds: [str] = line[1].split(';')
        result: {str, int} = get_nb_for_each_color(rounds)

        # check if the results make the game impossible
        add: bool = True
        for color in color_max_val_dict.keys():
            if result[color] > color_max_val_dict[color]:
                add = False
                break
        if add:
            sum_no_game += no_game

print(sum_no_game)
