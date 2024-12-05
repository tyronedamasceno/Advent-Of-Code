from collections import defaultdict

with open('inp.txt') as f:
    lines = f.read().split('\n')

k = lines.index('')
rules = lines[:k]
updates = [list(map(int, l.split(','))) for l in lines[k + 1:]]

tmp = defaultdict(set)

for rule in rules:
    a, b = map(int, rule.split('|'))
    tmp[a].add(b)

ans = 0

for upd in updates:
    seen = set()
    f = True
    for x in upd:
        if seen & tmp[x]:
            f = False
            break
        seen.add(x)
    if f:
        ans += upd[len(upd) // 2]

print(ans)
