with open("inp.txt") as f:
    lines = f.read().split("\n")
    lines = [list(map(int, l.split())) for l in lines]


def check_safety(report):
    k = report[1] - report[0]
    if k == 0 or abs(k) not in (1, 2, 3):
        return False

    for i in range(2, len(report)):
        k2 = report[i] - report[i - 1]
        if k2 == 0 or abs(k2) not in (1, 2, 3):
            return False
        if (k > 0 and k2 < 0) or (k < 0 and k2 > 0):
            return False
    return True


ans = 0

for report in lines:
    if check_safety(report):
        ans += 1
        continue

    backup = report[:]

    for i in range(len(report)):
        report.pop(i)
        if check_safety(report):
            ans += 1
            break
        report = backup[:]


print(ans)
