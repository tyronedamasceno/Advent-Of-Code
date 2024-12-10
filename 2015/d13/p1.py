from itertools import permutations

with open('inp.txt') as f:
    lines = f.read().splitlines()

happiness = {}
guests = set()

for line in lines:
    p1, _, s, h, _, _, _, _, _, _, p2 = line[:-1].split()
    h = int(h) if s == 'gain' else -int(h)
    happiness[(p1, p2)] = h
    guests.add(p1)

ans = -1
for pm in permutations(guests):
    tmp = 0
    for i, g in enumerate(pm):
        tmp += happiness[(g, pm[((i + 1) % len(guests))])]
        tmp += happiness[(g, pm[((i - 1) % len(guests))])]
    ans = max(ans, tmp)

print(ans)
