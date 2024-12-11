from collections import defaultdict

with open('inp.txt') as f:
    line = f.read()

stones = defaultdict(int)
for s in map(int, line.split()):
    stones[s] += 1


for _ in range(75):
    new = defaultdict(int)
    for k in stones.keys():
        if k == 0:
            new[1] += stones[k]
        elif len(str(k)) % 2 == 0:
            sst = str(k)
            a, b = sst[:len(sst) // 2], sst[len(sst) // 2:]
            new[int(a)] += stones[k]
            new[int(b)] += stones[k]
        else:
            new[k * 2024] += stones[k]

    stones = new

print(sum(stones.values()))
