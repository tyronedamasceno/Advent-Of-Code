with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0

x = lines.index('')
freshs = list(tuple(map(int, t.split('-'))) for t in lines[:x])
freshs = list(set(freshs))

freshs.sort()
new_ranges = []

cur = freshs[0]

for rg in freshs[1:]:
    if cur[1] >= rg[0]:
        cur = (cur[0], max(cur[1], rg[1]))
        continue
    new_ranges.append(tuple(cur))
    cur = rg

if cur:
    new_ranges.append(tuple(cur))


ans = sum((b-a+1) for a, b in new_ranges)
print(ans)
