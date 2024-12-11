from math import sqrt

with open('inp.txt') as f:
    line = int(f.read())

k = 0
m = 0
while True:
    k += 1
    divs = {i for i in range(1, int(sqrt(k)) + 1) if k % i == 0}
    divs.update({k // d for d in divs})
    tmp = sum(divs) * 10
    if tmp > line:
        print(k)
        break
