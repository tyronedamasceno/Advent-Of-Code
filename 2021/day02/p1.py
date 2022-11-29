with open('inp.txt') as f:
    l = f.read().split('\n')

x, y = 0, 0

for k in l:
    cmd, pwr = k.split()
    pwr = int(pwr)
    if cmd == 'forward':
        x += pwr
    elif cmd == 'down':
        y += pwr
    elif cmd == 'up':
        y -= pwr

print(x*y)
