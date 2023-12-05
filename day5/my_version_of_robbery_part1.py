from intervaltree import IntervalTree, Interval
import time

start_time = time.time()
with open('input.txt', 'r') as f:
    seeds, *blocks = f.read().split('\n\n')

    seeds = list(map(int, seeds.split(':')[1].split()))

    for block in blocks:
        intervals = IntervalTree()
        for line in block.splitlines()[1:]:
            dest, source, span = map(int,line.split())
            intervals.add(Interval(source, source + span, dest - source))
        new = []
        for seed in seeds:
            interval = intervals[seed]
            if interval:
                new.append(seed + interval.pop().data)
            else:
                new.append(seed)
        seeds = new

    print(min(seeds))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"The code took {elapsed_time} seconds to run.")