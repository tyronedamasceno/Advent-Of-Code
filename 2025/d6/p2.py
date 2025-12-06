from math import prod

with open("inp.txt") as f:
    lines = f.read().splitlines()

ops = lines[-1].strip().split()
lines = [list(l) for l in lines[:-1]]

for j in range(len(lines[0])):
    exist = False
    for i in range(len(lines)):
        if lines[i][j] != " ":
            exist = True
            break
    if exist:
        for i in range(len(lines)):
            if lines[i][j] == " ":
                lines[i][j] = "x"

lines = ["".join(l).split() for l in lines]
cols = [[lines[j][i] for j in range(len(lines))] for i in range(len(lines[0]))]

ans = 0

for c, op in zip(cols, ops):
    verts = []
    for j in range(len(c[0])):
        tmp = ""
        for i in range(len(c)):
            if c[i][j] != "x":
                tmp += c[i][j]
        verts.append(int(tmp))
    if op == "+":
        ans += sum(verts)
    elif op == "*":
        ans += prod(verts)

print(ans)
