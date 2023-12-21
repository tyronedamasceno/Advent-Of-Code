with open("inp.txt") as f:
    lines = f.read().split('\n')

for i, l in enumerate(lines):
    if 'S' in l:
        start = i, l.find('S')
        break

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cur = {start}
for _ in range(64):
    nxt = set()
    for x, y in cur:
        for dx, dy in dirs:
            nx = dx + x
            ny = dy + y
            if nx < 0 or nx >= len(lines) or ny < 0 or ny >= len(lines[0]) or lines[nx][ny] == '#':
                continue
            nxt.add((nx, ny))
    cur = nxt

print(len(cur))
