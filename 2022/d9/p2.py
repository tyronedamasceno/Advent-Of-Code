with open("inp.txt") as f:
    moves = [x.split() for x in f.read().splitlines()]
    moves = [(a, int(b)) for a, b in moves]

tails = [(0, 0) for i in range(0, 10)]

visits = set()
visits.add(tails[9])
pos = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def compare_points(head, tail):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return tail

    sign_x = 0 if head[0] == tail[0] else (head[0] - tail[0]) / abs(head[0] - tail[0])
    sign_y = 0 if head[1] == tail[1] else (head[1] - tail[1]) / abs(head[1] - tail[1])

    tail = tail[0] + sign_x, tail[1] + sign_y

    return tail


for to, qtt in moves:
    for _ in range(qtt):
        tails[0] = (tails[0][0] + pos[to][0], tails[0][1] + pos[to][1])

        for i in range(1, 10):
            tails[i] = compare_points(tails[i - 1], tails[i])

        visits.add(tails[-1])

print(len(visits))
