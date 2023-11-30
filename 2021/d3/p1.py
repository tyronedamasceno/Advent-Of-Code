with open("inp.txt") as f:
    l = f.read().split()

d = {i: {"0": set(), "1": set()} for i in range(len(l[0]))}

for s in l:
    for i, b in enumerate(s):
        d[i][b].add(s)

gamma = ""
epsilon = ""

for i in range(len(l[0])):
    if len(d[i]["0"]) > len(d[i]["1"]):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))
