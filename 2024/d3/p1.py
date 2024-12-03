import re

with open("inp.txt") as f:
    lines = f.read()
    # lines = [list(map(int, l.split())) for l in lines]

matches = re.findall(r"mul\((-?\d+),(-?\d+)\)", lines)
ans = 0
for a, b in matches:
    ans += (int(a) * int(b))

print(ans)
