with open("inp.txt") as f:
    lines = f.read().split('\n')


def _get_next(x, y, dir, s):
    d = {
        'R': (0, 1),
        'L': (0, -1),
        'D': (1, 0),
        'U': (-1, 0),
    }
    a, b = d[dir]
    return x + (a * s), y + (b * s)


points = [(0, 0)]
b = 0  # trench spaces

for l in lines:
    _, _, c = l.split()
    c = c[2:-1]
    k = int(c[:-1], 16)
    b += k
    d = 'RDLU'[int(c[-1])]
    points.append(_get_next(*points[-1], d, k))

# shoelace formula
A = sum(
    points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1])
    for i in range(len(points))
) / 2

# pick theorem reverted
i = A - b / 2 + 1  # inner area

ans = i + b
print(ans)
