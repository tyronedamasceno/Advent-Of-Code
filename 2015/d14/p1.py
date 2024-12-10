with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = (-1, 'a')
for line in lines:
    k = line.split()
    reindeer = k[0]
    speed = int(k[3])
    duration = int(k[6])
    rest = int(k[-2])

    dist = 0
    m = 0
    flying = True
    # breakpoint()
    while m < 2503:
        if not flying:
            m += rest
            flying = True
            continue

        to_go = min(duration, 2503 - m)
        dist += speed * to_go
        m += to_go
        flying = False

    ans = max(ans, (dist, reindeer))

print(ans)
