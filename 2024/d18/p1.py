from queue import Queue

with open('inp.txt') as f:
    lines = [tuple(map(int, l.split(','))) for l in f.read().splitlines()]

corrupted = set(lines[:1024])

st = 0, 0
end = 70, 70
seen = set()

q = Queue()
q.put((*st, 0))

while not q.empty():
    x, y, k = q.get()
    if (x, y) == end:
        print(k)
        break

    if (x, y) in seen:
        continue

    seen.add((x, y))

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in corrupted:
            q.put((nx, ny, k + 1))
