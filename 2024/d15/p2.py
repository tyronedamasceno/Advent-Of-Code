from copy import deepcopy
from tqdm import tqdm

with open('inp.txt') as f:
    tmp_grid, rules = f.read().split('\n\n')

tmp_grid = [list(l) for l in tmp_grid.splitlines()]

grid = []
for l in tmp_grid:
    tmp = []
    for x in l:
        if x == '#':
            tmp.extend(['#', '#'])
        elif x == 'O':
            tmp.extend(['[', ']'])
        elif x == '.':
            tmp.extend(['.', '.'])
        else:
            tmp.extend(['@', '.'])
    grid.append(tmp)

for i, l in enumerate(grid):
    if '@' in l:
        rx, ry = i, l.index('@')
        break


def print_grid():
    for l in grid:
        print(''.join(l))


rmap = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}

for rule in tqdm(rules):
    if rule == '\n':
        continue
    dx, dy = rmap[rule]

    to_move = [(rx, ry)]
    i = 0
    flag = False

    while i < len(to_move):
        x, y = to_move[i]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == '[':
            if (nx, ny) not in to_move:
                to_move.append((nx, ny))
            if (nx, ny + 1) not in to_move:
                to_move.append((nx, ny + 1))
        elif grid[nx][ny] == ']':
            if (nx, ny) not in to_move:
                to_move.append((nx, ny))
            if (nx, ny - 1) not in to_move:
                to_move.append((nx, ny - 1))
        elif grid[nx][ny] == '#':
            flag = True
            break

        i += 1

    if flag:
        continue
    tmp = deepcopy(grid)
    for x, y in to_move:
        tmp[x][y] = '.'
    for x, y in to_move:
        tmp[x + dx][y + dy] = grid[x][y]

    grid = tmp
    rx += dx
    ry += dy

ans = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '[':
            ans += (100 * i + j)
print(ans)
