from intervaltree import IntervalTree, Interval

inputs, *blocks = open("input.txt").read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    all_intervals = IntervalTree()
    for line in block.splitlines()[1:]:
        dest, source, span = map(int, line.split())
        all_intervals.add(Interval(source, source + span, dest - source))
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        intervals = all_intervals[start:end]
        intervals = sorted(intervals)
        last_end = start
        while intervals:
            interval = intervals.pop()
            new.append((max(interval.begin, last_end) + interval.data, min(interval.end, end) + interval.data))
            if interval.begin > last_end:
                new.append((last_end, interval.begin))
            last_end = interval.end

        if last_end < end:
            new.append((last_end, end))
        if last_end == start:
            new.append((last_end, end))
    seeds = new

print(min(seeds)[0])
