with open('inp.txt') as f:
    lines = f.read().split('\n')

ans = 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        try:
            d1 = ''.join(lines[i + k][j + k] for k in range(3))
            d2 = ''.join(lines[i - k + 2][j + k] for k in range(3))
        except IndexError:
            continue
        if d1 in ('MAS', 'SAM') and d2 in ('MAS', 'SAM'):
            ans += 1

print(ans)
