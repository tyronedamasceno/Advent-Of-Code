with open('inp.txt') as f:
    grid = f.read().splitlines()
    grid = [list(map(int, l)) for l in grid]

seen = 0


def score(x, y):
    if grid[x][y] == 9:
        global seen
        seen += 1
        return

    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
            continue

        if grid[x][y] + 1 == grid[x + dx][y + dy]:
            score(x + dx, y + dy)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            score(i, j)

print(seen)
