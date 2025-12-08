from collections import defaultdict
from math import prod

with open("inp.txt") as f:
    boxes = [tuple(map(int, l.split(","))) for l in f.read().splitlines()]


def dist(p, q):
    p1, p2, p3 = p
    q1, q2, q3 = q
    return (p1 - q1) ** 2 + (p2 - q2) ** 2 + (p3 - q3) ** 2


dists = {}
adj = defaultdict(list)

for i, t1 in enumerate(boxes):
    for t2 in boxes[i + 1 :]:
        dists[(t1, t2)] = dist(t1, t2)

shortest = sorted(dists.items(), key=lambda it: it[1])

seen = set()

for pair, _ in shortest:
    t1, t2 = pair
    seen.add(t1)
    seen.add(t2)
    if len(seen) == len(boxes):
        print(t1[0] * t2[0])
        break
