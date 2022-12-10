with open('inp.txt') as f:
    lines = f.read().splitlines()

x = 1
cycle = 0
so = {20, 60, 100, 140, 180, 220}

ans = 0

for i, line in enumerate(lines):
    if line == 'noop':
        cycle += 1
        if cycle in so:
            ans += (cycle * x)
    else:
        cycle += 1
        if cycle in so:
            ans += (cycle * x)
        cycle += 1
        _, k = line.split()
        if cycle in so:
            ans += (cycle * x)
        x += int(k)

print(ans)
