import re
from collections import defaultdict

with open('inp.txt') as f:
    lines = f.read().splitlines()

d = defaultdict(int)

for line in lines:
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))

    for _ in range(100):
        px += vx
        px %= 101
        py += vy
        py %= 103

    d[(px, py)] += 1

ans = 1
c = 0
for i in range(101 // 2):
    for j in range(103 // 2):
        c += d[(i, j)]
ans *= c

c = 0
for i in range(101 // 2 + 1, 101):
    for j in range(103 // 2):
        c += d[(i, j)]
ans *= c

c = 0
for i in range(101 // 2):
    for j in range(103 // 2 + 1, 103):
        c += d[(i, j)]
ans *= c

c = 0
for i in range(101 // 2 + 1, 101):
    for j in range(103 // 2 + 1, 103):
        c += d[(i, j)]
ans *= c

print(ans)
