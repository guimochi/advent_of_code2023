import time
import re

start_time = time.time()


def insert_char(string, char, index):
    return string[:index] + char + string[index:]


def replace_char(string, char, index):
    return string[:index] + char + string[index + 1:]


with open('input.txt', 'r') as f:
    univ = [line.replace('\n', "") for line in f]

    empty_row = [r for r, l in enumerate(univ) if '#' not in l]
    empty_col = [c for c, ch in enumerate(zip(*univ)) if '#' not in ch]
    offset = 0
    for r in empty_row:
        univ.insert(r + offset, '.' * len(univ[0]))
        offset += 1
    print(empty_row)
    offset = 0
    for c in empty_col:
        for r in range(len(univ)):
            univ[r] = insert_char(univ[r], '.', c + offset)
        offset += 1

    gals = []
    i = 1
    for r, line in enumerate(univ):
        matches = re.finditer('#', line)
        for match in matches:
            gals.append((r, match.start()))
            univ[r] = replace_char(univ[r], str(i), match.start())
            i += 1
    print(gals)
    for u in univ:
        print(u)

    dist = 0
    for i in range(len(gals) - 1):
        for j in range(i + 1, len(gals)):
            ax, ay = gals[i]
            bx, by = gals[j]
            d = abs(ax - bx) + abs(ay - by)
            print(univ[ax][ay] + " -> " + univ[bx][by] + " = " + str(d))
            dist += d

    print(dist)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")
