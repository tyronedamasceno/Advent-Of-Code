with open("inp.txt") as f:
    l = [int(n) for n in f.read().split("\n")]

x = 0

for i in range(1, len(l)):
    if l[i] > l[i - 1]:
        x += 1

print(x)
