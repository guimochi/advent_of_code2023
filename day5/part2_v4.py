import re
from typing import Dict, Tuple, List
from multiprocessing import Pool

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
    nbs = [int(match.group()) for match in re.finditer(r'\d+', first_line)]
    return [(nbs[i], nbs[i] + nbs[i + 1]) for i in range(0, len(nbs), 2)]


def get_paths(a_to_b: Dict[Tuple[str, str], Dict[Tuple[int, int], int]]):
    return {key[0]: key[1] for key in a_to_b.keys()}


def get_parcours(paths: Dict[str, str], start: str):
    last_step = start
    next_step = paths[start]
    parcours: List[Tuple[str, str]] = []
    while next_step:
        parcours.append((last_step, next_step))
        last_step = next_step
        next_step = paths.get(next_step)
    return parcours


def find_closest_location_for_seed(seed: Tuple[int, int], a_to_b: Dict[Tuple[str, str], IntervalTree],
                                   parcours: List[Tuple[str, str]]) -> int:
    print("pool")
    return min(go_to_end(a_to_b, parcours, i) for i in range(seed[0], seed[1]))


def find_closest_location(list_seeds: List[Tuple[str, str]], a_to_b: Dict[Tuple[str, str], IntervalTree],
                          parcours: List[Tuple[str, str]]) -> int:
    with Pool() as pool:
        results = pool.starmap(find_closest_location_for_seed, [(seed, a_to_b, parcours) for seed in list_seeds])
    return min(results)


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

if __name__ == "__main__":
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
        closest_location = find_closest_location(seeds, a_to_b, parcours)
        print(closest_location)
