from queue import Queue

with open("inp.txt") as f:
    lines = f.read().split('\n')


def get_next(x, y, dir):
    d = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0),
        '^': (-1, 0),
    }
    a, b = d[dir]
    return ((x + a, y + b), dir)


def get_energized_tiles(ini, ini_dir):
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
            q.put(get_next(x, y, dir))
        elif lines[x][y] == '-':
            if dir in ('>', '<'):
                q.put(get_next(x, y, dir))
            else:
                q.put(get_next(x, y, '>'))
                q.put(get_next(x, y, '<'))
        elif lines[x][y] == '|':
            if dir in ('v', '^'):
                q.put(get_next(x, y, dir))
            else:
                q.put(get_next(x, y, '^'))
                q.put(get_next(x, y, 'v'))
        elif lines[x][y] == '/':
            if dir == '>':
                q.put(get_next(x, y, '^'))
            elif dir == '<':
                q.put(get_next(x, y, 'v'))
            elif dir == '^':
                q.put(get_next(x, y, '>'))
            elif dir == 'v':
                q.put(get_next(x, y, '<'))
        elif lines[x][y] == '\\':
            if dir == '>':
                q.put(get_next(x, y, 'v'))
            elif dir == '<':
                q.put(get_next(x, y, '^'))
            elif dir == '^':
                q.put(get_next(x, y, '<'))
            elif dir == 'v':
                q.put(get_next(x, y, '>'))

    return len(set(a for a, _ in seen))


ans = -1
for i in range(len(lines)):
    ans = max(ans, get_energized_tiles((i, 0), '>'))
    ans = max(ans, get_energized_tiles((i, len(lines[0]) - 1), '<'))

for j in range(len(lines[0])):
    ans = max(ans, get_energized_tiles((0, j), 'v'))
    ans = max(ans, get_energized_tiles((len(lines) - 1, j), 'v'))

print(ans)
