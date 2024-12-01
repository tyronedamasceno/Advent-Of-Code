from collections import defaultdict
from queue import Queue


with open("inp2.txt") as f:
    lines = f.read().split('\n')

g = defaultdict(set)

for line in lines:
    src, dsts = line.split(': ')
    for dst in dsts.split():
        g[src].add(dst)
        g[dst].add(src)


def bipartition(graph, start):
    q = Queue()
    q.put(start)
    sets = {start: 1}

    while not q.empty():
        n = q.get()

        l = list(graph[n])
        for adj in l:
            if adj not in sets:
                sets[adj] = 2 if sets[n] == 1 else 1
                q.put(adj)
            elif sets[adj] == sets[n]:
                print(adj, n)
                graph[adj].remove(n)
                graph[n].remove(adj)

    set_a = [node for node, set_num in sets.items() if set_num == 1]
    set_b = [node for node, set_num in sets.items() if set_num == 2]

    return set_a, set_b


a, b = bipartition(g, src)
print(len(a), len(b))
