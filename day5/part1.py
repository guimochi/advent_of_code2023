import re
from typing import Dict, Tuple, List


def create_map(lines):
    lines.reverse()
    a_to_b: Dict[Tuple[str, str], Dict[Tuple[int, int], int]] = {}
    i = 0
    while lines:
        line = lines.pop()
        a, b = line.replace(' map:\n', "").split('-to-')
        a_to_b[(a, b)] = {}
        # check if lines is empty or line is an empty string
        while lines:
            i += 1
            line = lines.pop()
            if line == "\n":
                break
            destination, source, span = map(int, line.split())
            offset = destination - source
            a_to_b[(a, b)][(source, source + span - 1)] = offset

    return a_to_b


def get_seeds(first_line):
    nbs = re.finditer(r'\d+', first_line)
    return [int(nb.group()) for nb in nbs]


def get_paths(a_to_b: Dict[Tuple[str, str], Dict[Tuple[int, int], int]]):
    dict = {}
    for key in a_to_b.keys():
        dict[key[0]] = key[1]
    return dict


def get_parcours(paths: Dict[str, str], start: str):
    last_step = start
    next_step = paths[start]
    parcours: List[Tuple[str, str]] = []
    while next_step:
        parcours.append((last_step, next_step))
        last_step = next_step
        next_step = paths.get(next_step)
    return parcours


def find_closest_location(seeds: List[int], parcours: List[Tuple[str, str]],
                          a_to_b: Dict[Tuple[str, str], Dict[Tuple[int, int], int]]):
    smallest_value: int = 10 ** 10
    step: int
    for seed in seeds:
        step = seed
        # loop through all places to go, conversion is the point a to b
        for conversion in parcours:
            for tuple_span in a_to_b[conversion]:
                if tuple_span[0] <= step <= tuple_span[1]:
                    step = step + a_to_b[conversion][tuple_span]
                    break

        if step < smallest_value:
            smallest_value = step
    return smallest_value


with (open("input.txt", "r") as f):
    lines = f.readlines()
    # get seeds to check
    seeds: List[int] = get_seeds(lines[0])
    # create map that takes point a to b in key and a map save what offset to add. The offset are kept in a tuple that
    # express the range with is impacted by the offset
    a_to_b: Dict[Tuple[str, str], Dict[Tuple[int, int], int]] = create_map(lines[2:])
    # get the path
    paths: Dict[str, str] = get_paths(a_to_b)
    # get the parcours that needs to be made
    start = 'seed'
    parcours: List[Tuple[str, str]] = get_parcours(paths, start)
    # find the closest location
    closest_location: int = find_closest_location(seeds, parcours, a_to_b)
    print(closest_location)
    #answer = 177942185