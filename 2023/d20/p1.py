from collections import defaultdict
from queue import Queue

with open("inp.txt") as f:
    lines = f.read().split('\n')

flip_state = defaultdict(bool)
conj_memo = defaultdict(dict)
types = {}
wires = {}
hi = 0
lo = 0

for line in lines:
    mod, dsts = line.split(' -> ')
    if mod == 'broadcaster':
        broadcaster = dsts.split(', ')
        continue
    t, m = mod[:1], mod[1:]
    types[m] = t
    wires[m] = dsts.split(', ')


conjs = {m for m, t in types.items() if t == '&'}
for src, dsts in wires.items():
    for conj in set(dsts) & conjs:
        conj_memo[conj][src] = 0

q = Queue()
for _ in range(1000):
    lo += 1  # push button
    for d in broadcaster:
        q.put(('broadcaster', d, 0))

    while not q.empty():
        pr, m, sig = q.get()
        if sig == 0:
            lo += 1
        else:
            hi += 1

        if m not in types:
            continue

        if types[m] == '%' and sig == 1:
            continue
        if types[m] == '%':
            flip_state[m] = 1 - flip_state[m]
            for w in wires[m]:
                q.put((m, w, flip_state[m]))
            continue

        conj_memo[m][pr] = sig
        nxt = 1 - all(conj_memo[m].values())
        for w in wires[m]:
            q.put((m, w, nxt))

print(lo, hi)
print(lo * hi)
