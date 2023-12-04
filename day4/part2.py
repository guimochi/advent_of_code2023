import re
from typing import List, Tuple

digit_pattern = re.compile(r'\d+')
dict_cards: {int, set[str], set[str]}


# Scratchcard class
class Scratchcard:
    def __init__(self, number: int, winning_values: set[str], actual_values: set[str]):
        self.number = number
        self.winning_values = winning_values
        self.actual_values = actual_values

    # get the number of reward for the scratchcard
    def get_nb_reward(self):
        nb_reward = 0
        for winning_value in self.winning_values:
            if winning_value in self.actual_values:
                nb_reward += 1
        return nb_reward

    # get the list of reward for the scratchcard
    # TODO this function create a new Scratchcard object for each reward, it could be optimized by creating a hashmap
    #  with the line number as key and a scratchcard object as value
    def get_rewards(self):
        return [Scratchcard(i, dict_cards.get(i)[0], dict_cards.get(i)[1])
                for i in range(self.number + 1, self.number + self.get_nb_reward() + 1)
                if dict_cards.get(i) is not None]


# create a dict with line number as key and a tuple of winning values and actual values as value
def get_dict_cards(rl):
    dict_cards: {int, set[str], set[str]} = {}
    for line in rl:
        card, num_values = line.split(":")
        int_card = int(re.search(digit_pattern, card).group())
        winning_part, actual_part = num_values.split('|')
        win_nbs = set(winning_part.split())
        actual_nbs = set(actual_part.split())
        dict_cards[int_card] = win_nbs, actual_nbs
    return dict_cards


# recursive function to get the total number of scratches
def get_all_scratches(list_scratches: List[Scratchcard]):
    total: int = 0
    for scratch in list_scratches:
        total += (1 + get_all_scratches(scratch.get_rewards()))
    return total


def transform_to_scratches(dict_cards):
    return [Scratchcard(key, dict_cards[key][0], dict_cards[key][1]) for key in dict_cards.keys()]


with (open("input.txt", "r") as f):
    # create the initial hashmap of scratchcard
    dict_cards: {int, set[str], set[str]} = get_dict_cards(f.readlines())
    # transform the hashmap to a list of scratchcard
    list_scratches: List[Scratchcard] = transform_to_scratches(dict_cards)
    # get the total number of scratches
    nb_scratches: int = get_all_scratches(list_scratches)
    print(nb_scratches)
