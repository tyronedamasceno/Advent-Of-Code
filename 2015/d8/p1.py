with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0

for line in lines:
    tot = len(line)
    stored = 0

    i = 1
    while i < len(line) - 1:
        stored += 1
        if line[i] == '\\':
            if line[i + 1] in ('\\', '"'):
                i += 1
            elif line[i + 1] == 'x':
                i += 3
        i += 1

    ans += (tot - stored)

print(ans)
