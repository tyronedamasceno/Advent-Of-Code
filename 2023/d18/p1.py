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
    d, k, _ = l.split()
    b += int(k)
    points.append(_get_next(*points[-1], d, int(k)))

# shoelace formula
A = sum(
    points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1])
    for i in range(len(points))
) / 2

# pick theorem reverted
i = A - b / 2 + 1  # inner area

ans = i + b
print(ans)
