from collections import defaultdict

with open("inp.txt") as f:
    dd = defaultdict(int)
    for k in f.read().split("\n"):
        p1, p2 = k.split(" -> ")
        x1, y1 = [int(i) for i in p1.split(",")]
        x2, y2 = [int(i) for i in p2.split(",")]

        if x1 == x2:
            for yi in range(min(y1, y2), max(y1, y2) + 1):
                dd[(x1, yi)] += 1
        elif y1 == y2:
            for xi in range(min(x1, x2), max(x1, x2) + 1):
                dd[(xi, y1)] += 1
        else:
            x_sign = 1 if x1 < x2 else -1
            y_sign = 1 if y1 < y2 else -1
            range_x = range(x1, x2 + x_sign, x_sign)
            range_y = range(y1, y2 + y_sign, y_sign)
            for xi, yj in zip(range_x, range_y):
                dd[(xi, yj)] += 1

print(sum(x > 1 for x in dd.values()))
