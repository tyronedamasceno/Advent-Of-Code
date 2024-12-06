with open('inp.txt') as f:
    grid = [list(l) for l in f.read().split('\n')]

didx = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
seen = set()

for i, l in enumerate(grid):
    if '^' in l:
        gi, gj = i, l.index('^')
        break

goi, goj = gi, gj


def check_loop():
    gi, gj = goi, goj
    seen = set()
    didx = 0
    while True:
        if (gi, gj, didx) in seen:
            return True

        seen.add((gi, gj, didx))

        ni = gi + dirs[didx][0]
        nj = gj + dirs[didx][1]

        if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
            return False

        if grid[ni][nj] == '#':
            didx += 1
            didx %= 4
        else:
            gi, gj = ni, nj


ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            print(i, j)
            grid[i][j] = '#'
            if check_loop():
                ans += 1
            grid[i][j] = '.'

print(ans)
