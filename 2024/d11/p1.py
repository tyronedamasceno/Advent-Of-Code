with open('inp.txt') as f:
    line = f.read()

stones = list(map(int, line.split()))

for _ in range(25):
    for i in range(len(stones) - 1, -1, -1):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            sst = str(stones[i])
            a, b = sst[:len(sst) // 2], sst[len(sst) // 2:]
            stones[i:i + 1] = [int(a), int(b)]
        else:
            stones[i] *= 2024

print(len(stones))
