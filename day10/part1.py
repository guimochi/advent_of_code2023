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
    return (maze[p[0]-1][p[1]], (p[0]-1, p[1]), 'S')

def get_e(p):
    return (maze[p[0]][p[1] + 1], (p[0], p[1] + 1), 'W')

def get_s(p):
    return (maze[p[0]+1][p[1]], (p[0]+1, p[1]), 'N')

def get_w(p):
    return (maze[p[0]][p[1] - 1], (p[0], p[1] - 1), 'E')

def get_exit(step):
    letter = step[0]
    p = step[1]
    # check if coming from south
    if step[2] == 'S':
        if letter == '|':
            return get_n(p)
        if letter == 'F':
            return get_e(p)
        if letter == '7':
            return get_w(p)

    # check if coming from west
    if step[2] == 'W':
        if letter == '-':
            return get_e(p)
        if letter == 'J':
            return get_n(p)
        if letter == '7':
            return get_s(p)

    # check if coming from north
    if step[2] == 'N':
        if letter == '|':
            return get_s(p)
        if letter == 'L':
            return get_e(p)
        if letter == 'J':
            return get_w(p)

    # check if coming from east
    if step[2] == 'E':
        if letter == '-':
            return get_w(p)
        if letter == 'L':
            return get_n(p)
        if letter == 'F':
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

dist = 1
step = entries[0]
dist_p = {dist: step}
while True:
    step = get_exit(step)
    if step[0] == 'S':
        break
    dist += 1
    dist_p[dist] = step
far = math.ceil(dist/2)
print(far)
print(dist_p[far])



end_time = time.time()
elapsed_time = end_time - start_time
print(f"The code took {elapsed_time} seconds to run.")