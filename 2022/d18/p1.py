with open("inp.txt") as f:
    lines = [[int(x) for x in line.split(",")] for line in f.read().split("\n")]


def is_connected(ca, cb):
    if ca[0] == cb[0] and ca[1] == cb[1] and abs(ca[2] - cb[2]) <= 1:
        return True
    if ca[0] == cb[0] and ca[2] == cb[2] and abs(ca[1] - cb[1]) <= 1:
        return True
    if ca[1] == cb[1] and ca[2] == cb[2] and abs(ca[0] - cb[0]) <= 1:
        return True
    return False


k = 0
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        if is_connected(lines[i], lines[j]):
            k += 1

print(6 * len(lines) - 2 * k)
