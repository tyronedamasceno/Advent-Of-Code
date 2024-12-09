from itertools import permutations

with open('inp.txt') as f:
    lines = f.read().splitlines()

dists = {}
cities = set()

for line in lines:
    c1, _, c2, _, d = line.split()
    cities.update({c1, c2})
    dists[(c1, c2)] = int(d)
    dists[(c2, c1)] = int(d)

ans = 9999999999999

for p in permutations(cities):
    tmp = 0
    for i in range(1, len(cities)):
        tmp += dists[(p[i - 1], p[i])]

    ans = min(ans, tmp)

print(ans)
