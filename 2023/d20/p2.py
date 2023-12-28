from collections import defaultdict
from math import lcm
from queue import Queue

with open("inp.txt") as f:
    lines = f.read().split('\n')

flip_state = defaultdict(bool)
conj_memo = defaultdict(dict)
types = {}
wires = {}

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

base = next(m for m, dsts in wires.items() if 'rx' in dsts)
seen = {m: False for m, dsts in wires.items() if base in dsts}
cycles = {}

q = Queue()
btn = 0

flag = False
while True:
    btn += 1
    for d in broadcaster:
        q.put(('broadcaster', d, 0))

    while not q.empty():
        pr, m, sig = q.get()

        if m not in types:
            continue

        if m == base and sig == 1:
            seen[pr] = True
            if pr not in cycles:
                cycles[pr] = btn
            if all(seen.values()):
                flag = True
                break

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
    if flag:
        break

ans = lcm(*cycles.values())
print(ans)
