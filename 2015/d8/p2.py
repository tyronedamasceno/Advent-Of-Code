with open('inp.txt') as f:
    line = f.read()

cur = 0
for i, d in enumerate(line):
    if d == '(':
        cur += 1
    else:
        cur -= 1
    if cur == -1:
        print(i + 1)
        break
