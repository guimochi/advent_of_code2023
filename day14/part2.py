import time

start_time = time.time()

with open("test.txt", "r") as f:
    grid = [line for line in f.read().split("\n")]

    r_obj = {}
    c_obj = {}

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == ".":
                continue
            if not r_obj.get(r):
                r_obj[r] = [[], []]
            r_obj[r][ch == "O"].append(c)
            if not c_obj.get(c):
                c_obj[c] = [[], []]
            c_obj[c][ch == "O"].append(r)

    # to move north
    for c, (rocks, balls) in c_obj.items():
        last_place = 0
        place = []
        for rock in rocks:
            place.extend(
                [
                    i
                    for i in range(
                        last_place,
                        last_place
                        + len([ball for ball in balls if last_place <= ball < rock]),
                    )
                ]
            )
            if len(place) == len(balls):
                break
            last_place = rock + 1
        place.extend(
            [i for i in range(last_place, last_place + len(balls) - len(place))]
        )
        c_obj[c][1] = place

    print(c_obj)
    len_grid = len(grid)
    total = sum(len_grid - ball for rocks, balls in c_obj.values() for ball in balls)
    print(total)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
