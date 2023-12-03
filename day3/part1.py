import re
from typing import List, Dict, Iterator

digit_pattern = re.compile(r'\d+')

with (open("input.txt", "r") as f):
    lines = f.readlines()
    unique_chars = {char for line in lines for char in line if
                    not char.isdigit() and char != '.' and char != '\n'}
    str_unique_chars = '[\\' + '\\'.join(unique_chars) + ']'
    symbols_pattern = re.compile(str_unique_chars)


def create_list_line_special_match(lines: List[str]):
    list_line_special_match: [(int, re.Match)] = []
    i: int = 0
    for line in lines:
        # get all symbol matches
        matches = re.finditer(symbols_pattern, line)
        for match in matches:
            # add them to the list as a tuple(num_line, symbol_match)
            list_line_special_match.append((i, match))
        i += 1
    return list_line_special_match


def get_adjacent_coordinates(special_coordinate: (int, int), adjacent_coordinates: set[(int, int)]):
    i_line: int = special_coordinate[0]
    i_col: int = special_coordinate[1]
    # this is to add top-left,top, top-right & bot-left, bot, bot-right
    for i in range(-1, 2):
        # add all coordinates above
        adjacent_coordinates.add((i_line - 1, i_col + i))
        # add all coordinates below
        adjacent_coordinates.add((i_line + 1, i_col + i))
    # add left coordinate
    adjacent_coordinates.add((special_coordinate[0], special_coordinate[1] - 1))
    # add right coordinate
    adjacent_coordinates.add((special_coordinate[0], special_coordinate[1] + 1))


def find_adjacent_coordinates(list_line_symbol_match: [(int, re.Match)]):
    # this is made as a set to gain some time, doing so will prevent to check multiple times on the same coordinates
    candidate_coordinates: set[(int, int)] = set()
    for special_match in list_line_symbol_match:
        symbol_coordinate = (special_match[0], special_match[1].start())
        get_adjacent_coordinates(symbol_coordinate, candidate_coordinates)
    return candidate_coordinates


def create_dict_line_nb_matches(lines: List[str]):
    dict_line_nb_matches: Dict[int, List[re.Match]] = {}
    i: int = 0
    for line in lines:
        # the casting is crucial. Without casting the iterator as a list, I can only iterate it once
        matches = list(re.finditer(digit_pattern, line))
        # add all matches in the dict where num_line is the key and the list of matches of numbers as value
        dict_line_nb_matches[i] = matches
        i += 1
    return dict_line_nb_matches


def get_total_sum(candidate_coordinates: [(int, int)], dict_line_nb_matches: Dict[int, List[re.Match]]):
    # create a set to prevent adding the same number twice
    candidates: {re.Match} = set()
    for coordinate in candidate_coordinates:
        i_line = coordinate[0]
        if i_line in dict_line_nb_matches:
            for nb_match in dict_line_nb_matches[i_line]:
                # check if any part of the number is in the candidate coordinate
                if nb_match.start() <= coordinate[1] < nb_match.end():
                    candidates.add(nb_match)

    # add the value of all candidates
    total: int = 0
    for candidate in candidates:
        total += int(candidate.group())
    return total


with (open("input.txt", "r") as f):
    lines = f.readlines()
    # list of tuple with nb line and the match of a special chr
    list_line_special_match: [(int, re.Match)] = create_list_line_special_match(lines)
    # all places where we look should for a number
    candidate_coordinates: set[(int, int)] = find_adjacent_coordinates(list_line_special_match)
    # hashmap with num of line as key and list of matches of numbers
    dict_line_nb_matches: Dict[int, List[re.Match]] = create_dict_line_nb_matches(lines)
    # get the total sum of all real candidates numbers
    total = get_total_sum(candidate_coordinates, dict_line_nb_matches)
    print('total :', total)
