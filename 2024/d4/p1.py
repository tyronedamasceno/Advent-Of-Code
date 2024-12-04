with open('inp.txt') as f:
    lines = f.read().split('\n')

ans = 0

for l in lines:
    ans += l.count('XMAS')
    ans += l.count('SAMX')

lines_t = [''.join([row[i] for row in lines]) for i in range(len(lines[0]))]

for l in lines_t:
    ans += l.count('XMAS')
    ans += l.count('SAMX')

for i in range(len(lines)):
    for j in range(len(lines[0])):
        try:
            tmp = ''.join(lines[i + k][j + k] for k in range(4))
            if tmp == 'XMAS' or tmp == 'SAMX':
                ans += 1
        except IndexError:
            continue

for i in range(len(lines)):
    for j in range(3, len(lines[0])):
        try:
            tmp = ''.join(lines[i + k][j - k] for k in range(4))
            if tmp == 'XMAS' or tmp == 'SAMX':
                ans += 1
        except IndexError:
            continue

print(ans)
