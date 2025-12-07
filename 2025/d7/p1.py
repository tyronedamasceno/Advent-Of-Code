from queue import Queue

with open("inp.txt") as f:
    grid = f.read().splitlines()

q = Queue()
seen = set()
splitters = set()

q.put((0, grid[0].index("S")))

while not q.empty():
    x, y = q.get()
    if (x, y) in seen:
        continue
    seen.add((x, y))
    if x == len(grid) - 1:
        continue
    if grid[x + 1][y] == ".":
        q.put((x + 1, y))
    else:
        splitters.add((x + 1, y))
        q.put((x + 1, y - 1))
        q.put((x + 1, y + 1))

print(len(splitters))
