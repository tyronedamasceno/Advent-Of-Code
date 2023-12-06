with open("inp.txt") as f:
    lines = f.read().split('\n')

time = int("".join(lines[0].split(':')[-1].split()))
dist = int("".join(lines[1].split(':')[-1].split()))

for i in range(time + 1):
    v = i
    mdist = v * (time - i)
    if mdist > dist:
        print(time - (2 * v) + 1)
        break
