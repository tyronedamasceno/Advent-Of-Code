with open('inp.txt') as f:
    line = f.read()

diskmap = []
idx = 0
ranges = {}
for i, v in enumerate(line):
    if i % 2 == 0:
        a = len(diskmap)
        diskmap.extend(int(v) * [idx])
        b = len(diskmap)
        ranges[idx] = (a, b)
        idx += 1
    else:
        diskmap.extend(int(v) * '.')

file = idx - 1

while file >= 0:
    a, b = ranges[file]
    for i in range(a):
        if diskmap[i:i + (b - a)] == ['.'] * (b - a):
            diskmap[i:i + (b - a)], diskmap[a:b] = diskmap[a:b], diskmap[i:i + (b - a)]
            break
    file -= 1

ans = 0
for i, v in enumerate(diskmap):
    if v != '.':
        ans += (i * int(v))

print(ans)
