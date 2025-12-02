with open("inp.txt") as f:
    lines = f.read().splitlines()

pos = 50
ans = 0

for line in lines:
    q = int(line[1:])

    if line[0] == 'L':
        q = -q

    pos += q
    pos %= 100
    if pos == 0:
        ans += 1

print(ans)

