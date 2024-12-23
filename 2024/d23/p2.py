from collections import defaultdict

with open('inp.txt') as f:
    lines = f.read().splitlines()

conns = defaultdict(set)

for line in lines:
    c1, c2 = line.split('-')
    conns[c1].add(c2)
    conns[c2].add(c1)

completes = set()


def find_completes(comp, cur):
    key = tuple(sorted(cur))
    if key in completes:
        return
    completes.add(key)
    for conn in conns[comp]:
        if conn in cur:
            continue
        if not all(conn in conns[query] for query in cur):
            continue

        find_completes(conn, cur | {conn})


for comp in conns.keys():
    find_completes(comp, {comp})

print(','.join(sorted(completes, key=len, reverse=True)[0]))
