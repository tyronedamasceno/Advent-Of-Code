from collections import defaultdict
from string import digits

with open("inp2.txt") as f:
    lines = f.read().split('\n')

ans = 0
sd = defaultdict(bool)
gears = []
numbers = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '*':
            gears.append((i, j))

seen = set()
k = ''
pos = []


for i, line in enumerate(lines):
    if k:
        numbers.append((k, list(pos)))
        k = ''
        pos = []
    for j, c in enumerate(line):
        if k and c not in digits:
            numbers.append((k, list(pos)))
            k = ''
            pos = []
        if c in digits:
            k += c
            pos.append((i, j))


def _check_adjacencies(xg, yg):
    tmp = []
    adjs = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    for number, positions in numbers:
        for a, b in adjs:
            if (xg + a, yg + b) in positions:
                tmp.append(int(number))
                break
    return tmp


for gear in gears:
    x = _check_adjacencies(*gear)
    if len(x) == 2:
        ans += (x[0] * x[1])


print(ans)
