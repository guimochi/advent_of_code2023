import time

start_time = time.time()

with open("test.txt", "r") as f:
    grid = [line for line in f.read().split("\n")]

    len_grid = len(grid)

    total_weight = 0
    # check col by col
    for c, chs in enumerate(zip(*grid)):
        # last obstacle seen
        last_obstacle = -1
        for r, ch in enumerate(chs):
            if ch == "#":
                last_obstacle = r
            if ch == "O":
                last_obstacle += 1
                total_weight += len_grid - last_obstacle
    print(total_weight)


end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
