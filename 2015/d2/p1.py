with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0
for l in lines:
    ds = list(map(int, l.split('x')))
    ds.sort()
    l, w, h = ds
    ans += (2 * l * w + 2 * w * h + 2 * h * l)
    ans += l * w

print(ans)
