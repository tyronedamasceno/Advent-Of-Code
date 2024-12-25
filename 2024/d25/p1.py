with open('inp.txt') as f:
    schemes = f.read().split('\n\n')

schemes = [[list(row) for row in scheme.splitlines()] for scheme in schemes]

keys = []
locks = []

for scheme in schemes:
    if scheme[0] == list('#####'):
        locks.append(list(scheme))
    elif scheme[0] == list("....."):
        keys.append(list(scheme))

ans = 0
for lock in locks:
    transl = [[lock[j][i] for j in range(len(lock))] for i in range(len(lock[0]))]
    countl = [row.index('.') for row in transl]
    for key in keys:
        transk = [[key[j][i] for j in range(len(key))] for i in range(len(key[0]))]
        countk = [row[::-1].index('.') for row in transk]
        s = [a + b for a, b in zip(countl, countk)]
        if all(x <= 7 for x in s):
            ans += 1

print(ans)
