from collections import defaultdict

with open('inp.txt') as f:
    lines = f.read().splitlines()

r = len(lines)
c = len(lines[0])
antennas = defaultdict(list)


for i, line in enumerate(lines):
    for j, k in enumerate(line):
        if k != '.':
            antennas[k].append((i, j))

ans = set()

for _, locs in antennas.items():
    for i, (ax, ay) in enumerate(locs):
        for bx, by in locs[i + 1:]:
            dx = abs(ax - bx)
            dy = abs(ay - by)

            if ax < bx and ay > by:
                an1 = min(ax, bx) - dx, max(ay, by) + dy
                an2 = max(ax, bx) + dx, min(ay, by) - dy
            else:
                an1 = min(ax, bx) - dx, min(ay, by) - dy
                an2 = max(ax, bx) + dx, max(ay, by) + dy

            if 0 <= an1[0] < r and 0 <= an1[1] < c:
                ans.add(an1)
            if 0 <= an2[0] < r and 0 <= an2[1] < c:
                ans.add(an2)

print(len(ans))
