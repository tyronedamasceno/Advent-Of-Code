with open('inp.txt') as f:
    line = f.read()

diskmap = []
idx = 0
for i, v in enumerate(line):
    if i % 2 == 0:
        diskmap.extend(int(v) * [idx])
        idx += 1
    else:
        diskmap.extend(int(v) * '.')

x = 0
y = len(diskmap) - 1

while x < y:
    if diskmap[x] != '.':
        x += 1
        continue
    if diskmap[y] == '.':
        y -= 1
        continue

    diskmap[x], diskmap[y] = diskmap[y], diskmap[x]

ans = 0
for i, v in enumerate(diskmap):
    if v != '.':
        ans += (i * int(v))

print(ans)
