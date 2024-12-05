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

rules = tmp

wrongs = []

for upd in updates:
    seen = set()
    f = True
    for x in upd:
        if seen & rules[x]:
            f = False
            break
        seen.add(x)
    if not f:
        wrongs.append(upd)

ans = 0
for upd in wrongs:
    for i in range(len(upd)):
        for j in range(i + 1, len(upd)):
            if upd[i] in rules[upd[j]]:
                upd[i], upd[j] = upd[j], upd[i]

    ans += upd[len(upd) // 2]

print(ans)
