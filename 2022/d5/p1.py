from collections import defaultdict
import queue
import string

with open('inp.txt') as f:
    lines = f.read().split('\n')

cols = {}
cols_i = {}

for i, x in enumerate(lines):
    if set(x) & set(string.digits):
        a = i
        for idx, k in enumerate(x):
            if k in string.digits:
                cols[k] = idx
                cols_i[idx] = k
        break

stacks = defaultdict(queue.LifoQueue)

for i in range(a-1, -1, -1):
    for idx, v in enumerate(lines[i]):
        if v in string.ascii_uppercase:
            stacks[cols_i[idx]].put(v)

for line in lines[a+2:]:
    _, qtt, _, f, _, t = line.split()
    for _ in range(int(qtt)):
        stacks[t].put(stacks[f].get())

ans = ''
for _, s in stacks.items():
    ans += s.get()

print(ans) 
