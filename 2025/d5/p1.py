with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0

x = lines.index('')
freshs = list(tuple(map(int, t.split('-'))) for t in lines[:x])
avail = list(map(int, lines[x+1:]))

for ing in avail:
    for a, b in freshs:
        if a <= ing <= b:
            ans += 1
            break

print(ans)
