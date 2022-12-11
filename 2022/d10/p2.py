with open('inp.txt') as f:
    lines = f.read().splitlines()

reg_x = 1
cycle = -1
ans = []

def _check_sprite(c, r):
    if c % 40 in range(r-1, r+2):
        return '#'
    return ' '

for line in lines:
    if line == 'noop':
        cycle += 1
        ans.append(_check_sprite(cycle, reg_x))
    else:
        cycle += 1
        ans.append(_check_sprite(cycle, reg_x))

        cycle += 1
        ans.append(_check_sprite(cycle, reg_x))

        k = int(line.split()[1])
        reg_x += k

for i in range(0, 240, 40):
    print(''.join(ans[i:i+40]))
