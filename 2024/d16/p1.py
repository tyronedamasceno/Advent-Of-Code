from collections import defaultdict
from queue import PriorityQueue

with open('inp.txt') as f:
    grid = f.read().splitlines()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i, line in enumerate(grid):
    for j, k in enumerate(line):
        if k == 'S':
            sx, sy = i, j
        if k == 'E':
            ex, ey = i, j

dists = defaultdict(lambda: float('inf'))
seen = set()
q = PriorityQueue()

dists[(sx, sy)] = 0
q.put((0, sx, sy, 0, 1))

dx, dy = (0, 1)

while not q.empty():
    dist, x, y, dx, dy = q.get()

    if (x, y) in seen:
        continue

    seen.add((x, y))

    for tx, ty in dirs:
        if grid[x + tx][y + ty] == '#':
            continue
        if (dx, dy) == (tx, ty):
            dists[(x + tx, y + ty)] = min(dists[(x + tx, y + ty)], dists[(x, y)] + 1)
        else:
            dists[(x + tx, y + ty)] = min(dists[(x + tx, y + ty)], dists[(x, y)] + 1001)
        q.put((dists[(x + tx, y + ty)], x + tx, y + ty, tx, ty))

print(dists[(ex, ey)])
