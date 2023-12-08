import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


with open("inp.txt") as f:
    lines = f.read().split('\n')

seq = lines[0]
d = {}
curs = []
for line in lines[2:]:
    src, dst = line.split(' = ')
    if src[-1] == 'A':
        curs.append(src)
    d[src] = dst[1:-1].split(', ')

ans = 0
i = 0
zs = {}
while True:
    ans += 1

    flag = True
    for j in range(len(curs)):
        if seq[i] == 'L':
            curs[j] = d[curs[j]][0]
        else:
            curs[j] = d[curs[j]][1]

        if curs[j][-1] == 'Z' and j not in zs:
            zs[j] = ans

    if len(zs) == len(curs):
        break

    i += 1
    i %= len(seq)

mins = list(zs.values())
ans = mins[0]
for m in mins[1:]:
    ans = lcm(ans, m)

print(ans)
