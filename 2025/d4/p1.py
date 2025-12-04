with open('inp.txt') as f:
    grid = f.read().splitlines()

ans = 0

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
            ans += 1

print(ans)
