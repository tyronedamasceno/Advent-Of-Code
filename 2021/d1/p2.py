with open("inp.txt") as f:
    l = [int(n) for n in f.read().split("\n")]

x = 0

l2 = [sum(l[i: i + 3]) for i in range(len(l) - 2)]

x = 0

for i in range(1, len(l2)):
    if l2[i] > l2[i - 1]:
        x += 1

print(x)
