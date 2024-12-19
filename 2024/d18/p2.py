from queue import Queue

with open('inp.txt') as f:
    lines = [tuple(map(int, l.split(','))) for l in f.read().splitlines()]

st = 0, 0
end = 70, 70

for i in range(1, len(lines)):
    corrupted = set(lines[:i])

    q = Queue()
    q.put((*st, 0))
    seen = set()

    reached = False

    while not q.empty():
        x, y, k = q.get()
        if (x, y) == end:
            reached = True
            break

        if (x, y) in seen:
            continue

        seen.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in corrupted:
                q.put((nx, ny, k + 1))

    if not reached:
        print(i, lines[i - 1])
        break
