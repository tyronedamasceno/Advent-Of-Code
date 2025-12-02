with open("inp.txt") as f:
    lines = f.read().splitlines()

pos = 50
ans = 0

for line in lines:
    q = int(line[1:])

    for _ in range(q):
        if line[0] == 'L':
            pos -= 1
        else:
            pos += 1
        pos %= 100

        if pos == 0:
            ans += 1

print(ans)
