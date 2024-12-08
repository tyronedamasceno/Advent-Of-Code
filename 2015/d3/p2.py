with open('inp.txt') as f:
    line = f.read()

ans = set()
cur = 0, 0
dm = {
    '^': (-1, 0),
    '<': (0, -1),
    'v': (1, 0),
    '>': (0, 1),
}

ans.add(cur)
for d in line[::2]:
    x, y = cur
    nx, ny = dm[d]
    cur = x + nx, y + ny
    ans.add(cur)

cur = 0, 0
for d in line[1::2]:
    x, y = cur
    nx, ny = dm[d]
    cur = x + nx, y + ny
    ans.add(cur)

print(len(ans))
