with open('inp.txt') as f:
    grid = [list(l) for l in f.read().split('\n')]

didx = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
seen = set()

for i, l in enumerate(grid):
    if '^' in l:
        gi, gj = i, l.index('^')


while True:
    seen.add((gi, gj))
    ni = gi + dirs[didx][0]
    nj = gj + dirs[didx][1]

    if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
        break

    if grid[ni][nj] in ('.', '^'):
        gi, gj = ni, nj
    else:
        didx += 1
        didx %= 4
        ni = gi + dirs[didx][0]
        nj = gj + dirs[didx][1]
        gi, gj = ni, nj

for x, y in seen:
    grid[x][y] = 'X'

print(len(seen))
