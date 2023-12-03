import re
from typing import List, Dict, Tuple, Set

digit_pattern = re.compile(r'\d+')
gear_pattern = re.compile(r'[*]')


def create_list_line_gear_match(lines: List[str]):
    list_line_special_match: [(int, re.Match)] = []
    i: int = 0
    for line in lines:
        # get all symbol matches
        matches = re.finditer(gear_pattern, line)
        for match in matches:
            # add them to the list as a tuple(num_line, symbol_match)
            list_line_special_match.append((i, match))
        i += 1
    return list_line_special_match


def get_adjacent_coordinates(gear_coordinate_match: (int, int, re.Match),
                             set_adjacent_coordinate_gear_match: set[(int, int, re.Match)]):
    i_line: int = gear_coordinate_match[0]
    i_col: int = gear_coordinate_match[1]
    # this is to add top-left,top, top-right & bot-left, bot, bot-right
    for i in range(-1, 2):
        # add all coordinates above
        set_adjacent_coordinate_gear_match.add((i_line - 1, i_col + i, gear_coordinate_match[2]))
        # add all coordinates below
        set_adjacent_coordinate_gear_match.add((i_line + 1, i_col + i, gear_coordinate_match[2]))
    # add left coordinate
    set_adjacent_coordinate_gear_match.add((gear_coordinate_match[0], gear_coordinate_match[1] - 1,
                                            gear_coordinate_match[2]))
    # add right coordinate
    set_adjacent_coordinate_gear_match.add((gear_coordinate_match[0], gear_coordinate_match[1] + 1,
                                            gear_coordinate_match[2]))


def find_adjacent_coordinates(list_line_gear_match: [(int, re.Match)]):
    # this is made as a set to gain some time, doing so will prevent to check multiple times on the same coordinates
    candidate_coordinates: set[(int, int, re.Match)] = set()
    for line_gear_match in list_line_gear_match:
        gear_coordinate_match: (int, int, re.Match) = (line_gear_match[0], line_gear_match[1].start(), line_gear_match)
        get_adjacent_coordinates(gear_coordinate_match, candidate_coordinates)
    return candidate_coordinates


def create_dict_line_set_nb_matches(lines: List[str]):
    dict_line_nb_matches: Dict[int, Set[re.Match]] = {}
    i: int = 0
    for line in lines:
        # the casting is crucial. Without casting the iterator as a list, I can only iterate it once
        matches = set(re.finditer(digit_pattern, line))
        # add all matches in the dict where num_line is the key and the list of matches of numbers as value
        dict_line_nb_matches[i] = matches
        i += 1
    return dict_line_nb_matches


def get_total_sum(candidate_coordinates: [(int, int, re.Match)], dict_line_nb_matches: Dict[int, Set[re.Match]]):
    # dict to associate a gear with all numbers adjacent to him
    dict_gear_match_nb_matches: Dict[re.Match, Set[re.Match]] = {}

    for coordinate in candidate_coordinates:
        i_line = coordinate[0]
        i_column = coordinate[1]
        if i_line in dict_line_nb_matches:
            for nb_match in dict_line_nb_matches[i_line]:
                # check if any part of the number is in the candidate coordinate
                if nb_match.start() <= i_column < nb_match.end():
                    # create the set if he doesn't exist yet
                    if coordinate[2] not in dict_gear_match_nb_matches:
                        dict_gear_match_nb_matches[coordinate[2]] = set()
                    dict_gear_match_nb_matches[coordinate[2]].add(nb_match)

    # add the value of all dict_coord_nb_matches
    total: int = 0
    for set_nb_match in dict_gear_match_nb_matches.values():
        # check if there is exactly 2 numbers adjacent to the gear
        if len(set_nb_match) != 2:
            continue
        product: int = 1
        for nb_match in set_nb_match:
            product *= int(nb_match.group())
        total += product
    return total


with (open("input.txt", "r") as f):
    lines = f.readlines()
    # list of tuple with nb line and the match of a special chr
    list_line_gear_match: [(int, re.Match)] = create_list_line_gear_match(lines)
    # hashmap with num of line as key and list of matches of numbers
    dict_line_set_nb_matches: Dict[int, Set[re.Match]] = create_dict_line_set_nb_matches(lines)
    # all places where we look should for a number and keep track of the gear associated with this coordinate
    candidate_coordinates: set[(int, int, re.Match)] = find_adjacent_coordinates(list_line_gear_match)
    # get the total sum of all real candidates numbers
    total = get_total_sum(candidate_coordinates, dict_line_set_nb_matches)
    print('total :', total)
