with open("inp.txt") as f:
    lines = f.read().split('\n')

times = [int(x) for x in lines[0].split(':')[-1].split()]
dists = [int(x) for x in lines[1].split(':')[-1].split()]

ans = 1

for time, dist in zip(times, dists):
    k = 0

    for i in range(time + 1):
        v = i
        mdist = v * (time - i)
        if mdist > dist:
            k += 1

    ans *= k

print(ans)
