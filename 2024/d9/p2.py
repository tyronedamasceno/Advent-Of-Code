with open('inp.txt') as f:
    line = f.read()

diskmap = []
idx = 0
ranges_f = {}
ranges_b = []
for i, v in enumerate(line):
    if i % 2 == 0:
        a = len(diskmap)
        diskmap.extend(int(v) * [idx])
        b = len(diskmap)
        ranges_f[idx] = (a, b)
        idx += 1
    else:
        a = len(diskmap)
        diskmap.extend(int(v) * '.')
        b = len(diskmap)
        ranges_b.append((a, b))

file = idx - 1

while file >= 0:
    a, b = ranges_f[file]
    for i, (x, y) in enumerate(ranges_b):
        if y > a:
            break
        if y - x >= b - a:
            diskmap[x:x + (b - a)], diskmap[a:b] = diskmap[a:b], diskmap[x:x + (b - a)]
            ranges_b[i] = (x + b - a, y)
            break
    file -= 1

ans = 0
for i, v in enumerate(diskmap):
    if v != '.':
        ans += (i * int(v))

print(ans)
