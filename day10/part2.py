import math
import re
import time

n_conn = '|', 'L', 'J'
e_conn = '-', 'L', 'F'
s_conn = 'F', '|', '7'
w_conn = '-', 'J', '7'

start_time = time.time()


with open('input.txt', 'r') as f:
    maze = []
    i = 0
    start = None
    for line in f.readlines():
        if 'S' in line:
            start = (i, re.search('S', line).start())
        maze.append(line[:-1])
        i += 1
    print(maze)


def get_n(p):
    return [maze[p[0]-1][p[1]], (p[0]-1, p[1]), 'S']

def get_e(p):
    return [maze[p[0]][p[1] + 1], (p[0], p[1] + 1), 'W']

def get_s(p):
    return [maze[p[0]+1][p[1]], (p[0]+1, p[1]), 'N']

def get_w(p):
    return [maze[p[0]][p[1] - 1], (p[0], p[1] - 1), 'E']

def get_exit(step):
    letter = step[0]
    p = step[1]
    # check if coming from south
    if step[2] == 'S':
        if letter == '|':
            step.append('N')
            return get_n(p)
        if letter == 'F':
            step.append('E')
            return get_e(p)
        if letter == '7':
            step.append('W')
            return get_w(p)

    # check if coming from west
    if step[2] == 'W':
        if letter == '-':
            step.append('E')
            return get_e(p)
        if letter == 'J':
            step.append('N')
            return get_n(p)
        if letter == '7':
            step.append('S')
            return get_s(p)

    # check if coming from north
    if step[2] == 'N':
        if letter == '|':
            step.append('S')
            return get_s(p)
        if letter == 'L':
            step.append('E')
            return get_e(p)
        if letter == 'J':
            step.append('W')
            return get_w(p)

    # check if coming from east
    if step[2] == 'E':
        if letter == '-':
            step.append('W')
            return get_w(p)
        if letter == 'L':
            step.append('N')
            return get_n(p)
        if letter == 'F':
            step.append('S')
            return get_s(p)


# with open('test.txt', 'r') as f:
#     maze = []
#     i = 0
#     start = None
#     for line in f.readlines():
#         if 'S' in line:
#             start = (i, re.search('S', line).start())
#         maze.append(line[:-1])
#         i += 1

    # check top
entries = []
if get_n(start)[0] in s_conn:
    entries.append(get_n(start))
if get_e(start)[0] in w_conn:
    entries.append(get_e(start))
if get_s(start)[0] in n_conn:
    entries.append(get_s(start))
if get_w(start)[0] in e_conn:
    entries.append(get_w(start))

step = entries[0]
maze_parts = {step[1]: step}
while step[0] != 'S':
    step = get_exit(step)
    maze_parts[step[1]] = step

maze_parts[start].append(maze_parts[entries[0][1]][2])
print(maze_parts)

flag_up = False
total = 0
for r, line in enumerate(maze):
    for c, ch in enumerate(line):
        part = maze_parts.get((r, c))
        if not flag_up and part is None:
            continue
        if flag_up and part is None:
            total += 1
            continue
        if part[3] == 'S':
            flag_up = True
            continue
        if part[2] == 'S':
            flag_up = False
            continue

print(total)









end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")