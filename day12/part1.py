import time
import re

start_time = time.time()


def replace_springs(spring: str, combis: [str]):
    match = re.search(r"\?", spring)
    if match is None:
        combis.append(spring)
        return
    replace_springs(spring[: match.start()] + "#" + spring[match.start() + 1 :], combis)
    replace_springs(spring[: match.start()] + "." + spring[match.start() + 1 :], combis)


def check(combi: str, record):
    i_rec = 0
    c_spring = 0
    i = 0
    while i < len(combi):
        if combi[i] == "#":
            while i < len(combi) and combi[i] == "#":
                c_spring += 1
                i += 1
            if c_spring != record[i_rec]:
                return 0
            else:
                if i_rec == len(record) - 1:
                    if "#" in combi[i:]:
                        return 0
                    return 1
                i_rec += 1
                c_spring = 0
        i += 1
    return 0


check(".###........", [3, 2, 1])
with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        spring = line.split(" ")[0]
        record = list(map(int, line.split(" ")[1].split(",")))
        combis = []
        replace_springs(spring, combis)
        for combi in combis:
            ret = check(combi, record)
            total += ret
    print(total)

    pass

end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
