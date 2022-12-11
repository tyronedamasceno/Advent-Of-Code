with open('inp.txt') as f:
    moves = [x.split() for x in f.read().splitlines()]
    moves = [(a, int(b)) for a, b in moves]

head = (0,0)
tail = (0,0)

visits = set()
visits.add(tail)
pos = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

for to, qtt in moves:
    for _ in range(qtt):
        head = (head[0] + pos[to][0], head[1] + pos[to][1])
        
        if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
            continue

        sign_x = 0 if head[0] == tail[0] else (head[0] - tail[0]) / abs(head[0] - tail[0])
        sign_y = 0 if head[1] == tail[1] else (head[1] - tail[1]) / abs(head[1] - tail[1])

        tail = tail[0] + sign_x, tail[1] + sign_y

        visits.add(tail)

print(len(visits))
