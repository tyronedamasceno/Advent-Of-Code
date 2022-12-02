import math
from queue import Queue

with open('inp.txt') as f:
    m = [[int(x) for x in line] for line in f.read().split('\n')]

def _is_lower(m, i, j):
    if i > 0 and m[i][j] >= m[i-1][j]:
        return False
    if j > 0 and m[i][j] >= m[i][j-1]:
        return False
    if i < len(m) - 1 and m[i][j] >= m[i+1][j]:
        return False
    if j < len(m[0]) - 1 and m[i][j] >= m[i][j+1]:
        return False
    return True

def _basin_size(m, i, j):
    sz = 0
    visited = set()
    q = Queue()
    q.put((i, j))
    while not q.empty():
        x, y = q.get()
        if (x, y) in visited:
            continue
        sz += 1
        visited.add((x, y))
        if x > 0 and m[x][y] < m[x-1][y] and m[x-1][y] != 9:
            q.put((x-1, y))
        if y > 0 and m[x][y] < m[x][y-1] and m[x][y-1] != 9:
            q.put((x, y-1))
        if x < len(m) - 1 and m[x][y] < m[x+1][y] and m[x+1][y] != 9:
            q.put((x+1, y))
        if y < len(m[0]) - 1 and m[x][y] < m[x][y+1] and m[x][y+1] != 9:
            q.put((x, y+1))
    return sz

lower_points = []

for i in range(len(m)):
    for j in range(len(m[0])):
        if _is_lower(m, i, j):
            lower_points.append((i, j))

basins = []
for i, j in lower_points:
    basins.append(_basin_size(m, i, j))

print(math.prod(sorted(basins, reverse=True)[:3]))
