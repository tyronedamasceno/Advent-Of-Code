with open('inp.txt') as f:
    grid, rules = f.read().split('\n\n')

grid = [list(l) for l in grid.splitlines()]
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


def move(rx, ry, dx, dy):
    if grid[rx + dx][ry + dy] == '#':
        return False

    if grid[rx + dx][ry + dy] == '.':
        grid[rx][ry], grid[rx + dx][ry + dy] = grid[rx + dx][ry + dy], grid[rx][ry]
        return True

    if move(rx + dx, ry + dy, dx, dy):
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
        if grid[i][j] == 'O':
            ans += (100 * i + j)

print(ans)
