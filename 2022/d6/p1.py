with open("inp.txt") as f:
    k = f.read()

for i in range(len(k) - 4):
    if len(set(k[i: i + 4])) == 4:
        print(i + 4)
        break
