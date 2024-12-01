from collections import Counter

with open("inp.txt") as f:
    lines = f.read().split("\n")
    lines = [list(map(int, l.split())) for l in lines]

l1 = []
l2 = []
for l in lines:
    l1.append(l[0])
    l2.append(l[1])

c = Counter(l2)

ans = 0

for x in l1:
    ans += x * c[x]

print(ans)
