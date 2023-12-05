import re
from typing import Dict, Tuple, List

from intervaltree import IntervalTree, Interval


def create_map(lines):
    a_to_b: Dict[Tuple[str, str], IntervalTree] = {}
    while lines:
        line = lines.pop(0)
        a, b = line.replace(' map:\n', "").split('-to-')
        a_to_b[(a, b)] = IntervalTree()
        while lines:
            line = lines.pop(0)
            if line == "\n":
                break
            destination, source, span = map(int, line.split())
            offset = destination - source
            a_to_b[(a, b)].add(Interval(source, source + span, offset))
    return a_to_b


def get_seeds(first_line):
    nbs = list(re.finditer(r'\d+', first_line))
    seeds: List[Tuple[int, int]] = []
    while nbs:
        start = int(nbs.pop(0).group())
        end = start + int(nbs.pop(0).group())
        seeds.append((start, end))
    return seeds


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


def find_closest_location(list_seeds: List[Tuple[str, str]], parcours: List[Tuple[str, str]],
                          a_to_b: Dict[Tuple[str, str], Dict[Tuple[int, int], int]]):
    smallest_value: int = 10 ** 100
    step: int
    for tup_seed in list_seeds:
        for i in range(tup_seed[0], tup_seed[1]):
            step = i
            # loop through all places to go, conversion is the point a to b
            step = go_to_end(a_to_b, parcours, step)
            if step < smallest_value:
                smallest_value = step
    return smallest_value


def ranges_intersect(range1, range2):
    a, b = range1
    c, d = range2
    return not (b < c or d < a)


def go_to_end(a_to_b: Dict[Tuple[str, str], IntervalTree], parcours: List[Tuple[str, str]], step: int) -> int:
    for conversion in parcours:
        intervals = a_to_b[conversion][step]
        if intervals:
            step += intervals.pop().data
    return step


with (open("input.txt", "r") as f):
    lines = f.readlines()
    # get seeds to check
    seeds: List[Tuple[str, str]] = get_seeds(lines[0])
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
