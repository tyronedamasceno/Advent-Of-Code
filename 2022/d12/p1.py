from collections import defaultdict
from queue import PriorityQueue

def dijkstra(graph, st):
    dists = defaultdict(lambda : float('inf'))
    dists[st] = 0
    seen = set()

    pq = PriorityQueue()
    pq.put((0, st))

    while not pq.empty():
        (d, cur) = pq.get()
        seen.add(cur)

        for nxt in graph[cur]:
            if nxt not in seen:
                if dists[cur] + 1 < dists[nxt]:
                    dists[nxt] = dists[cur] + 1
                    pq.put((dists[nxt], nxt))
    return dists


with open('inp.txt') as f:
    grid = [list(line) for line in f.read().splitlines()]

s = None
e = None

adj = defaultdict(list)

for i, row in enumerate(grid):
    for j, column in enumerate(row):
        if column == 'S':
            s = (i, j)
            grid[i][j] = 'a'
        if column == 'E':
            e = (i, j)
            grid[i][j] = 'z'

        if i > 0 and ord(grid[i-1][j]) - ord(grid[i][j]) <= 1:
            adj[(i, j)].append((i-1, j))
        if j > 0 and ord(grid[i][j-1]) - ord(grid[i][j]) <= 1:
            adj[(i, j)].append((i, j-1))
        if i < len(grid) - 1 and ord(grid[i+1][j]) - ord(grid[i][j]) <= 1:
            adj[(i, j)].append((i+1, j))
        if j < len(grid[0]) - 1 and ord(grid[i][j+1]) - ord(grid[i][j]) <= 1:
            adj[(i, j)].append((i, j+1))

x = dijkstra(adj, s)
print(x[e] + 2)
