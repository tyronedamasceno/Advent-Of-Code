with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0

for line in lines:
    tot = len(line)
    stored = 2

    i = 0
    while i < len(line):
        stored += 1
        if line[i] in ('\\', '"'):
            stored += 1
        i += 1

    ans += (stored - tot)

print(ans)
