with open("inp.txt") as f:
    l = f.read().split()

d = {i: {"0": set(), "1": set()} for i in range(len(l[0]))}

for s in l:
    for i, b in enumerate(s):
        d[i][b].add(s)

to_oxygen = set(l)
to_carbon = set(l)

i_ox = 0
while len(to_oxygen) > 1:
    if len(d[i_ox]["1"] & to_oxygen) >= len(d[i_ox]["0"] & to_oxygen):
        to_oxygen -= d[i_ox]["0"]
    else:
        to_oxygen -= d[i_ox]["1"]
    i_ox += 1

i_carb = 0
while len(to_carbon) > 1:
    if len(d[i_carb]["0"] & to_carbon) <= len(d[i_carb]["1"] & to_carbon):
        to_carbon -= d[i_carb]["1"]
    else:
        to_carbon -= d[i_carb]["0"]
    i_carb += 1

print(int(to_oxygen.pop(), 2) * int(to_carbon.pop(), 2))
