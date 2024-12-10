with open('inp.txt') as f:
    grid = f.read().splitlines()
    grid = [list(map(int, l)) for l in grid]

seen = set()


def score(x, y):
    if grid[x][y] == 9:
        seen.add((x, y))
        return

    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if not (0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0])):
            continue

        if grid[x][y] + 1 == grid[x + dx][y + dy]:
            score(x + dx, y + dy)


ans = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            seen = set()
            score(i, j)
            ans += len(seen)

print(ans)
