with open("inp.txt") as f:
    lines = [
        [[int(z) for z in y.split("-")] for y in x.split(",")]
        for x in f.read().split("\n")
    ]

ans = 0
for a, b in lines:
    x0, y0 = a
    x1, y1 = b
    if (x0 <= x1 and y0 >= y1) or (x0 >= x1 and y0 <= y1):
        ans += 1

print(ans)
