with open("inp.txt") as f:
    reds = [tuple(map(int, t.split(","))) for t in f.read().splitlines()]

ans = -1
for i, (x1, y1) in enumerate(reds):
    for x2, y2 in reds[i + 1 :]:
        s = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        ans = max(ans, s)

print(ans)
