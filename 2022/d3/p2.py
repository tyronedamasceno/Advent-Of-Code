from string import ascii_lowercase

with open('inp.txt') as f:
    lines = f.read().split('\n')
    x = []
    for i in range(0, len(lines), 3):
        x.append(lines[i:i+3])

ans = 0
for g in x:
    k = (set(g[0]) & set(g[1]) & set(g[2])).pop()
    if k in ascii_lowercase:
        ans += (ord(k) - ord('a') + 1)
    else:
        ans += (ord(k) - ord('A') + 27)

print(ans)