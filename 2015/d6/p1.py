with open('inp.txt') as f:
    lines = f.read().splitlines()

grid = [[False for _ in range(1000)] for _ in range(1000)]


def tog(beg, end):
    bx, by = map(int, beg.split(','))
    ex, ey = map(int, end.split(','))
    for i in range(bx, ex + 1):
        for j in range(by, ey + 1):
            grid[i][j] = not grid[i][j]


def turn(beg, end, s):
    bx, by = map(int, beg.split(','))
    ex, ey = map(int, end.split(','))
    for i in range(bx, ex + 1):
        for j in range(by, ey + 1):
            grid[i][j] = (s == 'on')


for line in lines:
    l = line.split()
    beg, end = l[-3], l[-1]
    if l[0] == 'toggle':
        tog(beg, end)
    else:
        turn(beg, end, l[1])

print(sum(sum(l) for l in grid))
