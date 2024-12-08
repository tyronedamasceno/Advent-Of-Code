with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0
for line in lines:
    f = False
    for i in range(len(line) - 1):
        if line[i:i + 2] in line[i + 2:]:
            f = True
            break

    if not f:
        continue

    for i in range(len(line) - 2):
        if line[i] == line[i + 2]:
            ans += 1
            break

print(ans)
