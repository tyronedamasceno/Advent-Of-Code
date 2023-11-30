from collections import defaultdict

with open("inp.txt") as f:
    fishes = [int(x) for x in f.read().split(",")]

days = 256

cur = defaultdict(int)
for fish in fishes:
    cur[fish] += 1

while days:
    new = defaultdict(int)
    for i in range(9):
        if i == 0:
            new[8] = cur[i]
            new[6] = cur[i]
        else:
            new[i - 1] += cur[i]
    cur = new
    days -= 1

print(sum(cur.values()))
