with open("inp.txt") as f:
    lines = f.read().split('\n')

LOWER_BOUND = 200000000000000
UPPER_BOUND = 400000000000000
ans = 0

for idx, line1 in enumerate(lines):
    p1, v1 = line1.split('@')
    px1, py1, _ = map(int, p1.strip().split(', '))
    vx1, vy1, _ = map(int, v1.strip().split(', '))
    px12, py12 = px1 + vx1, py1 + vy1
    m1 = (py12 - py1) / (px12 - px1)
    b1 = py1 - m1 * px1
    for line2 in lines[idx + 1:]:
        p2, v2 = line2.split('@')
        px2, py2, _ = map(int, p2.strip().split(', '))
        vx2, vy2, _ = map(int, v2.strip().split(', '))
        px22, py22 = px2 + vx2, py2 + vy2
        m2 = (py22 - py2) / (px22 - px2)
        b2 = py2 - m2 * px2

        if m1 == m2:
            continue

        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        if not (LOWER_BOUND <= x <= UPPER_BOUND and LOWER_BOUND <= y <= UPPER_BOUND):
            continue

        if (x >= px1 and vx1 < 0) or (y >= py1 and vy1 < 0) or (x <= px1 and vx1 > 0) or (y <= py1 and vy1 > 0):
            continue

        if (x >= px2 and vx2 < 0) or (y >= py2 and vy2 < 0) or (x <= px2 and vx2 > 0) or (y <= py2 and vy2 > 0):
            continue

        ans += 1

print(ans)
