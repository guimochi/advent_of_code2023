import re
from part1 import get_nb_for_each_color

# 4 minutes


sum_power_sets: int = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(':')
        # get the results from the game
        rounds: [str] = line[1].split(';')
        result: {str, int} = get_nb_for_each_color(rounds)

        # multiply all result values
        product_game_set: int = 1
        for val_result in result.values():
            product_game_set *= val_result
        sum_power_sets += product_game_set

print(sum_power_sets)
