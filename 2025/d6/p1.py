from math import prod

with open("inp.txt") as f:
    lines = f.read().splitlines()

ops = lines[-1].strip().split()
lines = [list(map(int, l.strip().split())) for l in lines[:-1]]
cols = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]

ans = 0

for c, op in zip(cols, ops):
    if op == "+":
        ans += sum(c)
    elif op == "*":
        ans += prod(c)

print(ans)
