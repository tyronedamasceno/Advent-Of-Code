from queue import Queue

with open("inp.txt") as f:
    lines = f.read().split('\n')


def get_energized_tiles(ini, ini_dir):
    d = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0),
        '^': (-1, 0),
    }
    seen = set()
    q = Queue()
    q.put((ini, ini_dir))

    while not q.empty():
        (x, y), dir = q.get()
        if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[0]):
            continue

        if ((x, y), dir) in seen:
            continue

        seen.add(((x, y), dir))

        if lines[x][y] == '.':
            a, b = d[dir]
            q.put(((x + a, y + b), dir))
        elif lines[x][y] == '-':
            if dir in ('>', '<'):
                a, b = d[dir]
                q.put(((x + a, y + b), dir))
            else:
                a, b = d['>']
                q.put(((x + a, y + b), '>'))
                a, b = d['<']
                q.put(((x + a, y + b), '<'))
        elif lines[x][y] == '|':
            if dir in ('v', '^'):
                a, b = d[dir]
                q.put(((x + a, y + b), dir))
            else:
                a, b = d['^']
                q.put(((x + a, y + b), '^'))
                a, b = d['v']
                q.put(((x + a, y + b), 'v'))
        elif lines[x][y] == '/':
            if dir == '>':
                a, b = d['^']
                q.put(((x + a, y + b), '^'))
            elif dir == '<':
                a, b = d['v']
                q.put(((x + a, y + b), 'v'))
            elif dir == '^':
                a, b = d['>']
                q.put(((x + a, y + b), '>'))
            elif dir == 'v':
                a, b = d['<']
                q.put(((x + a, y + b), '<'))
        elif lines[x][y] == '\\':
            if dir == '>':
                a, b = d['v']
                q.put(((x + a, y + b), 'v'))
            elif dir == '<':
                a, b = d['^']
                q.put(((x + a, y + b), '^'))
            elif dir == '^':
                a, b = d['<']
                q.put(((x + a, y + b), '<'))
            elif dir == 'v':
                a, b = d['>']
                q.put(((x + a, y + b), '>'))

    return len(set(a for a, _ in seen))


ans = -1
for i in range(len(lines)):
    ans = max(ans, get_energized_tiles((i, 0), '>'))
    ans = max(ans, get_energized_tiles((i, len(lines[0]) - 1), '<'))

for j in range(len(lines[0])):
    ans = max(ans, get_energized_tiles((0, j), 'v'))
    ans = max(ans, get_energized_tiles((len(lines) - 1, j), 'v'))

print(ans)
