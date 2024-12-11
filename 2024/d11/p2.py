from collections import defaultdict

with open('inp.txt') as f:
    line = f.read()

stones = defaultdict(int)
for s in map(int, line.split()):
    stones[s] += 1


for _ in range(75):
    ks = list(stones.keys())
    new = defaultdict(int)
    for k in ks:
        if k == 0:
            new[1] += stones[k]
            stones.pop(k)
        elif len(str(k)) % 2 == 0:
            sst = str(k)
            a, b = sst[:len(sst) // 2], sst[len(sst) // 2:]
            new[int(a)] += stones[k]
            new[int(b)] += stones[k]
            stones.pop(k)
        else:
            new[k * 2024] += stones[k]
            stones.pop(k)

    stones = new

print(sum(stones.values()))
