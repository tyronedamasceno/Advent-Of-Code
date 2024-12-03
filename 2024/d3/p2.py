import bisect
import re

with open("inp.txt") as f:
    lines = f.read()

matches = [(match.group(0), match.start(), match.end()) for match in re.finditer(r"mul\((-?\d+),(-?\d+)\)", lines)]
dodonts = [(match.group(0), match.start(), match.end()) for match in re.finditer(r"do\(\)|don't\(\)", lines)]
ddidxs = [d[1] for d in dodonts]
ans = 0
for pat, i, j in matches:
    ddidx = bisect.bisect_left(ddidxs, i) - 1
    if ddidx >= 0 and dodonts[ddidx][0] == "don't()":
        continue
    a, b = pat[4:-1].split(',')
    ans += (int(a) * int(b))

print(ans)
