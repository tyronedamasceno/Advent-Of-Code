with open('inp.txt') as f:
    lines = f.read().splitlines()

grid = [[0 for _ in range(1000)] for _ in range(1000)]


def tog(beg, end):
    bx, by = map(int, beg.split(','))
    ex, ey = map(int, end.split(','))
    for i in range(bx, ex + 1):
        for j in range(by, ey + 1):
            grid[i][j] += 2


def turn(beg, end, s):
    bx, by = map(int, beg.split(','))
    ex, ey = map(int, end.split(','))
    for i in range(bx, ex + 1):
        for j in range(by, ey + 1):
            if s == 'on':
                grid[i][j] += 1
            else:
                grid[i][j] = max(0, grid[i][j] - 1)


for line in lines:
    l = line.split()
    beg, end = l[-3], l[-1]
    if l[0] == 'toggle':
        tog(beg, end)
    else:
        turn(beg, end, l[1])

print(sum(sum(l) for l in grid))
