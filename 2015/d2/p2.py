with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0
for l in lines:
    ds = list(map(int, l.split('x')))
    ds.sort()
    l, w, h = ds
    ans += (2 * l + 2 * w + l * h * w)

print(ans)
