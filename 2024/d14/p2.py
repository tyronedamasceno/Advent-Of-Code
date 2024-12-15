import re
from pprint import pprint

with open('inp.txt') as f:
    lines = f.read().splitlines()

robots = []

for line in lines:
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    robots.append([px, py, vx, vy])

i = 0

while True:
    i += 1
    grid = [['.' for _ in range(103)] for _ in range(101)]
    ps = set()
    for r in robots:
        r[0] += r[2]
        r[0] %= 101
        r[1] += r[3]
        r[1] %= 103
        grid[r[0]][r[1]] = '#'
        ps.add((r[0], r[1]))

    if len(ps) == 500:
        print(f'second {i}')
        pprint([''.join(l) for l in grid])
        break
