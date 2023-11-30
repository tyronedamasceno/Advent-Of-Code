from collections import defaultdict

with open('inp.txt') as f:
    lines = [
        [
            (int(k.split(',')[0]), int(k.split(',')[1]))
            for k in line.split(' -> ')
        ]
        for line in f.read().split('\n')
    ]

grid = defaultdict(bool)

maxy = float('-inf')
for line in lines:
    lx, ly = line[0]
    for point in line[1:]:
        px, py = point
        if lx != px:
            for k in range(min(lx, px),  max(lx, px)+1):
                grid[k, py] = True
        else:
            for k in range(min(ly, py),  max(ly, py)+1):
                grid[px, k] = True
        grid[point] = True
        maxy = max(maxy, point[1])
        lx, ly = point

start_point = 500, 0
count = 0

while True:
    count += 1
    x, y = start_point
    rest = False
    while not rest and y <= maxy:
        if not grid[(x, y + 1)]:
            y += 1
        elif not grid[(x - 1, y + 1)]:
            x -= 1
            y += 1
        elif not grid[(x + 1, y + 1)]:
            x += 1
            y += 1
        else:
            rest = True
            grid[(x, y)] = True

    if y > maxy:
        break

print(count-1)
