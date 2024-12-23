import itertools
from collections import defaultdict

with open('inp.txt') as f:
    lines = f.read().splitlines()

t_comps = set()
conns = defaultdict(set)

for line in lines:
    c1, c2 = line.split('-')
    if c1[0] == 't':
        t_comps.add(c1)
    if c2[0] == 't':
        t_comps.add(c2)
    conns[c1].add(c2)
    conns[c2].add(c1)

triplets = set()
for c in t_comps:
    for comb in itertools.combinations(conns[c], 2):
        c1, c2 = comb
        if c1 not in conns[c2]:
            continue
        triplets.add(tuple(sorted(comb + (c,))))

print(len(triplets))
