import re
from typing import Dict, Tuple, List


def create_map(lines):
    lines.reverse()
    a_to_b: Dict[Tuple[str, str], Dict[int, int]] = {}
    while lines:
        line = lines.pop()
        a, b = line.replace(' map:\n', "").split('-to-')
        a_to_b[(a, b)] = {}
        # check if lines is empty or line is an empty string
        while lines:
            line = lines.pop()
            if line == "\n":
                break
            destination, source, span = map(int, line.split())
            span_source = [i for i in range(source, source + span)]
            span_dest = [i for i in range(destination, destination + span)]
            for i in range(0, span):
                # I get the dict from a to b, so seed to soil, then I need to reach the dict that converts the number
                a_to_b[(a, b)][span_source[i]] = span_dest[i]

    return a_to_b


def get_seeds(first_line):
    nbs = re.finditer(r'\d+', first_line)
    return [int(nb.group()) for nb in nbs]


def get_paths(a_to_b):
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
                          a_to_b: Dict[Tuple[str, str], Dict[int, int]]):
    smallest_value: int = 10 ** 10
    step: int
    for seed in seeds:
        step = seed
        for conversion in parcours:
            if conversion in a_to_b.keys() and step in a_to_b[conversion].keys():
                step = a_to_b[conversion][step]
        if step < smallest_value:
            smallest_value = step
    return smallest_value


with (open("input.txt", "r") as f):
    lines = f.readlines()
    # get seeds to check
    seeds: List[int] = get_seeds(lines[0])
    # create map that will do the conversion
    a_to_b: Dict[Tuple[str, str], Dict[int, int]] = create_map(lines[2:])
    # get the path
    paths: Dict[str, str] = get_paths(a_to_b)
    # get the parcours that needs to be made
    start = 'seed'
    parcours: List[Tuple[str, str]] = get_parcours(paths, start)
    # find the closest location
    closest_location: int = find_closest_location(seeds, parcours, a_to_b)
    print(closest_location)