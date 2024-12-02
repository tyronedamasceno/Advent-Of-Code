with open("inp.txt") as f:
    lines = f.read().split("\n")
    lines = [list(map(int, l.split())) for l in lines]

ans = 0

for report in lines:
    k = report[1] - report[0]
    if k == 0 or abs(k) not in (1, 2, 3):
        continue
    f = True
    for i in range(2, len(report)):
        k2 = report[i] - report[i - 1]
        if k2 == 0 or abs(k2) not in (1, 2, 3):
            f = False
            break
        if (k > 0 and k2 < 0) or (k < 0 and k2 > 0):
            f = False
            break
    if f:
        ans += 1

print(ans)
