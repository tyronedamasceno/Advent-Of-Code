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

print_grid()

rmap = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}


def move(rx, ry, dx, dy):
    if grid[rx + dx][ry + dy] == '#':
        return False

    if grid[rx + dx][ry + dy] == '[':
        if move(rx + dx, ry + dy, dx, dy) and move(rx + dx, ry + dy + 1, dx, dy):
            grid[rx][ry], grid[rx + dx][ry + dy] = grid[rx + dx][ry + dy], grid[rx][ry]
            grid[rx][ry], grid[rx + dx][ry + dy + 1] = grid[rx + dx][ry + dy + 1], grid[rx][ry]
            return True

    if grid[rx + dx][ry + dy] == ']':
        if move(rx + dx, ry + dy, dx, dy) and move(rx + dx, ry + dy - 1, dx, dy):
            grid[rx][ry], grid[rx + dx][ry + dy] = grid[rx + dx][ry + dy], grid[rx][ry]
            grid[rx][ry], grid[rx + dx][ry + dy - 1] = grid[rx + dx][ry + dy - 1], grid[rx][ry]
            return True

    if grid[rx + dx][ry + dy] == '.':
        grid[rx][ry], grid[rx + dx][ry + dy] = grid[rx + dx][ry + dy], grid[rx][ry]
        return True

    return False


for rule in rules:
    if rule == '\n':
        continue
    dx, dy = rmap[rule]

    if move(rx, ry, dx, dy):
        rx, ry = rx + dx, ry + dy


ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '[':
            ans += (100 * i + j)

print_grid()
print(ans)
