with open('inp.txt') as f:
    fishes = [int(x) for x in f.read().split(',')]

days = 80
new = 0

while days:
    new = 0
    for i in range(len(fishes)):
        if fishes[i] == 0:
            fishes[i] = 6
            new += 1
        else:
            fishes[i] -= 1
    fishes += ([8] * new)
    days -= 1

print(len(fishes))
