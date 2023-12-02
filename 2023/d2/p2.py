from collections import defaultdict

with open("inp.txt") as f:
    lines = f.read().split('\n')

ans = 0
bads = set()

for line in lines:
    gn, rounds = line.split(':')
    gid = int(gn[5:])

    rounds = rounds.split(';')

    d = defaultdict(list)

    for round in rounds:
        round = [r.strip().split() for r in round.split(',')]
        for k, color in round:
            k = int(k)
            d[color].append(k)
    power = max(d['red']) * max(d['green']) * max(d['blue'])
    ans += power

print(ans)
