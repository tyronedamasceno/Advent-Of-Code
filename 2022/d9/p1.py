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
    # print(to, qtt)
    # if (to, qtt) == ('L', 3):
    #     breakpoint()
    for _ in range(qtt):
        head = (head[0] + pos[to][0], head[1] + pos[to][1])
        if abs(head[0]-tail[0]) > 1:
            if head[0] > tail[0]:
                tail = (tail[0] + 1, tail[1])
            else:
                tail = (tail[0] - 1, tail[1])
            if head[1] != tail[1]:
                tail = tail[0], head[1]
        if abs(head[1]-tail[1]) > 1:
            if head[1] > tail[1]:
                tail = (tail[0], tail[1] + 1)
            else:
                tail = (tail[0], tail[1] - 1)
            if head[0] != tail[0]:
                tail = head[0], tail[1]
        visits.add(tail)
        # print('after', head, tail)

print(len(visits))
