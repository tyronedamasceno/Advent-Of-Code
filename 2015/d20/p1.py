from math import sqrt

with open('inp.txt') as f:
    line = int(f.read())

k = 0
m = 0
while True:
    k += 1
    divs = set()
    for i in range(1, int(sqrt(k) + 1)):
        if k % i == 0:
            divs.add(i)
            divs.add(k // i)
    tmp = sum(divs) * 10
    if tmp > line:
        print(k, tmp)
        break
