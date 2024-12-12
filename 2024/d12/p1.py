from queue import Queue

with open('inp.txt') as f:
    grid = f.read().splitlines()

seen = set()
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in seen:
            continue
        seen.add((i, j))

        t = grid[i][j]
        region = set()
        q = Queue()
        q.put((i, j))

        p = 0
        while not q.empty():
            x, y = q.get()

            seen.add((x, y))
            region.add((x, y))
            p = 0
            for dx, dy in dd:
                if not (0 <= dx + x < len(grid) and 0 <= dy + y < len(grid[0])):
                    continue
                if (grid[x + dx][y + dy] == t) and ((x + dx, y + dy) not in seen):
                    q.put((x + dx, y + dy))
                    seen.add((x + dx, y + dy))

        p = 0
        for x, y in region:
            for dx, dy in dd:
                if (x + dx, y + dy) not in region:
                    p += 1

        ans += (len(region) * p)


print(ans)
