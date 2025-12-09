with open("inp.txt") as f:
    reds = [tuple(map(int, t.split(","))) for t in f.read().splitlines()]

boundary = set()

for i in range(len(reds)):
    x1, y1 = reds[i - 1]
    x2, y2 = reds[i]
    if x1 == x2:
        for j in range(min(y1, y2), max(y1, y2) + 1):
            boundary.add((x1, j))
    elif y1 == y2:
        for j in range(min(x1, x2), max(x1, x2) + 1):
            boundary.add((j, y1))

print(len(boundary))
ans = -1

for i, (x1, y1) in enumerate(reds):
    for x2, y2 in reds[i + 1 :]:
        f = True
        minx = min(x1, x2)
        maxx = max(x1, x2)
        miny = min(y1, y2)
        maxy = max(y1, y2)
        for bx, by in boundary:
            if minx < bx < maxx and miny < by < maxy:
                f = False
                break

        if f:
            s = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            ans = max(ans, s)

print(ans)
