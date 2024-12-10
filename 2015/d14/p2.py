with open('inp.txt') as f:
    lines = f.read().splitlines()


LIMIT = 2503
ans = (-1, 'a')
reindeers = {}
score = {}
position = {}
ranges = {}

for line in lines:
    k = line.split()
    reindeer = k[0]
    speed = int(k[3])
    duration = int(k[6])
    rest = int(k[-2])
    reindeers[reindeer] = (speed, duration, rest)
    score[reindeer] = 0
    position[reindeer] = 0
    ranges[reindeer] = []

    tmp = 0
    while tmp < LIMIT:
        ranges[reindeer].append((tmp, tmp + duration))
        tmp += (duration + rest)


for i in range(LIMIT):
    for r, (s, _, _) in reindeers.items():
        for rg in ranges[r]:
            if i in range(*rg):
                position[r] += s
    mp = max(position.values())
    for r in reindeers:
        if position[r] == mp:
            score[r] += 1


print(max(score.values()))
