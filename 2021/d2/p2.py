with open('inp.txt') as f:
    l = f.read().split('\n')

x, y, aim = 0, 0, 0

for k in l:
    cmd, pwr = k.split()
    pwr = int(pwr)
    if cmd == 'forward':
        x += pwr
        y += (aim * pwr)
    elif cmd == 'down':
        aim += pwr
    elif cmd == 'up':
        aim -= pwr

print(x*y)
