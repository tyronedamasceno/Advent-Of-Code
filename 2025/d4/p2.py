with open('inp.txt') as f:
    grid = [list(r) for r in f.read().splitlines()]

ans = 0

while True:
    to_remove = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                continue
            count = 0
            for ii, jj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if i + ii < 0 or i + ii >= len(grid) or j + jj < 0 or j + jj >= len(grid[0]):
                    continue
                if grid[i + ii][j + jj] == '@':
                    count += 1

            if count < 4:
                to_remove.append((i, j))
                ans += 1

    if not to_remove:
        break

    for i, j in to_remove:
        grid[i][j] = '.'

print(ans)
