from queue import Queue

with open("inp.txt") as f:
    lines = f.read().split('\n')

for i, l in enumerate(lines):
    if 'S' in l:
        start = i, l.index('S')
        break

q = Queue()
q.put(start)

seen = set()


def _get_directions(pipe):
    match pipe:
        case '|':
            return [(1, 0), (-1, 0)]
        case '-':
            return [(0, 1), (0, -1)]
        case 'F':
            return [(1, 0), (0, 1)]
        case 'J':
            return [(-1, 0), (0, -1)]
        case 'L':
            return [(-1, 0), (0, 1)]
        case '7':
            return [(1, 0), (0, -1)]


while not q.empty():
    i, j = q.get()
    seen.add((i, j))
    pipe = lines[i][j]
    if pipe == 'S':
        pipe = 'F'

    dirs = _get_directions(pipe)
    for x, y in dirs:
        nxt = (i + x, j + y)
        if nxt not in seen:
            q.put(nxt)

print(len(seen) / 2)
