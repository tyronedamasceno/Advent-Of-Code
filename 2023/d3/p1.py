from collections import defaultdict
from string import digits

with open("inp2.txt") as f:
    lines = f.read().split('\n')

ans = 0
sd = defaultdict(bool)
symbols = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c in symbols:
            sd[(i, j)] = True

seen = set()
k = ''
pos = []


def _check_adjacencies():
    adjs = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]
    for x, y in pos:
        for a, b in adjs:
            if (x + a, y + b) in sd:
                return int(k)

    return 0


for i, line in enumerate(lines):
    if k:
        ans += _check_adjacencies()
        k = ''
        pos = []
    for j, c in enumerate(line):
        if c in symbols or c == '.':
            ans += _check_adjacencies()
            k = ''
            pos = []
        if c in digits:
            k += c
            pos.append((i, j))

print(ans)
