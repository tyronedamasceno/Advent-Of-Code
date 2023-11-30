with open("inp.txt") as f:
    crabs = [int(x) for x in f.read().split(",")]


mi, ma = min(crabs), max(crabs)

better = float("inf")

for i in range(mi, ma + 1):
    better = min(better, sum(abs(k - i) for k in crabs))

print(better)
