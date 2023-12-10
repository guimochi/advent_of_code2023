from collections import deque

grid = open('test.txt').read().strip().splitlines()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == 'S':
            sr = r
            sc = c
            break
    # this propagates break
    else:
        continue
    break

# We will use a Bread first search. We scan in parallel
seen = {(sr, sc)}

q = deque([(sr, sc)])

while q:
    r, c = q.popleft()
    ch = grid[r][c]

    if r > 0 and (r - 1, c) not in seen and ch in 'S|JL' and grid[r - 1][c] in "|7F":
        seen.add((r - 1, c))
        q.append((r - 1, c))

    if r < len(grid) - 1 and (r + 1, c) not in seen and ch in 'S|7F' and grid[r + 1][c] in "|JL":
        seen.add((r + 1, c))
        q.append((r + 1, c))

    if c > 0 and (r, c - 1) not in seen and ch in 'S-J7' and grid[r][c - 1] in "-FL":
        seen.add((r, c - 1))
        q.append((r, c - 1))

    if c < len(grid[0]) - 1 and (r, c + 1) not in seen and ch in 'S-FL' and grid[r][c + 1] in "-J7":
        seen.add((r, c + 1))
        q.append((r, c + 1))
print(len(seen)// 2)