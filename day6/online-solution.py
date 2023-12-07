with open('input.txt', 'r') as f:
    times, distances = [list(map(int, ["".join(line.split(':')[1].split())])) for line in f.readlines()]
    n = 1
    # zip allows you to go through multiple arrays column by column
    for t, d in zip(times, distances):
        margin = 0
        for hold in range(1, t):
            if hold * (t - hold) > d:
                margin += 1
        n *= margin

    print(n)
    # Better way - start in middle and binary search / solve quadratique equation ourself / only look for one side and multiply by 2
