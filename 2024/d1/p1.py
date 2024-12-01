with open("inp.txt") as f:
    lines = f.read().split("\n")
    lines = [list(map(int, l.split())) for l in lines]

print(lines)
l1 = []
l2 = []
for l in lines:
    l1.append(l[0])
    l2.append(l[1])

l1.sort()
l2.sort()

ans = 0
for a, b in zip(l1, l2):
    ans += abs(a - b)

print(ans)
