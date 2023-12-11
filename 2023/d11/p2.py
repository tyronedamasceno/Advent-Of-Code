with open("inp.txt") as f:
    lines = f.read().split('\n')

lines = [list(l) for l in lines]

empty_lines = []
len_line = len(lines[0])
for idx, line in enumerate(lines):
    if set(line) == {'.'}:
        empty_lines.append(idx)

empty_columns = []
for idx in range(len_line):
    flag = True
    for j in range(len(lines)):
        if lines[j][idx] == '#':
            flag = False
            break
    if flag:
        empty_columns.append(idx)

galaxies = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            galaxies.append((i, j))

ans = 0

for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i + 1:]:
        ans += (abs(x1 - x2) + abs(y1 - y2))
        for l in empty_lines:
            if min(x1, x2) < l < max(x1, x2):
                ans += 999999
        for c in empty_columns:
            if min(y1, y2) < c < max(y1, y2):
                ans += 999999

print(ans)
