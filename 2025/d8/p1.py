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

for pair, _ in shortest[:1000]:
    t1, t2 = pair
    adj[t1].append(t2)
    adj[t2].append(t1)

seen = set()
circuits = []


def dfs(box):
    if box in seen:
        return
    seen.add(box)
    vis.add(box)
    for conn in adj[box]:
        dfs(conn)


for box in boxes:
    vis = set()
    if box not in seen:
        dfs(box)
    circuits.append(len(vis))

print(prod(sorted(circuits, reverse=True)[:3]))
