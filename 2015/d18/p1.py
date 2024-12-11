from copy import deepcopy

with open('inp.txt') as f:
    grid = f.read().splitlines()

grid = [list(l) for l in grid]
n = len(grid)


def solve(i, j):
    tmp = 0

    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if (x, y) == (0, 0):
                continue
            if 0 <= i + x < n and 0 <= j + y < n:
                tmp += (grid[i + x][j + y] == '#')

    if grid[i][j] == '#' and tmp in (2, 3):
        return '#'

    if grid[i][j] == '.' and tmp == 3:
        return '#'

    return '.'


for _ in range(100):
    new = deepcopy(grid)
    for i in range(n):
        for j in range(n):
            new[i][j] = solve(i, j)
    grid = deepcopy(new)

print(sum(sum(x == '#' for x in l) for l in grid))
