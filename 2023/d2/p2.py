from collections import defaultdict

with open("inp.txt") as f:
    lines = f.read().split('\n')

ans = 0
for line in lines:
    gn, rounds = line.split(':')
    gid = int(gn[5:])

    rounds = rounds.split(';')

    d = defaultdict(int)

    for round in rounds:
        round = [r.strip().split() for r in round.split(',')]
        for k, color in round:
            d[color] = max(d[color], int(k))
    power = d['red'] * d['green'] * d['blue']
    ans += power

print(ans)
