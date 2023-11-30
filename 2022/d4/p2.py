with open("inp.txt") as f:
    lines = [
        [[int(z) for z in y.split("-")] for y in x.split(",")]
        for x in f.read().split("\n")
    ]

ans = 0
for a, b in lines:
    x0, y0 = a
    x1, y1 = b
    k = False
    if x0 <= x1 and y0 >= x1:
        k = True
    if x0 >= x1 and x0 <= y1:
        k = True
    if x1 <= x0 and y1 >= x0:
        k = True
    if x1 >= x0 and x1 <= y0:
        k = True
    if k:
        ans += 1

print(ans)
