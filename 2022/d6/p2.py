with open("inp.txt") as f:
    k = f.read()

for i in range(len(k) - 14):
    if len(set(k[i: i + 14])) == 14:
        print(i + 14)
        break
