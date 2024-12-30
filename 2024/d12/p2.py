from collections import defaultdict
from queue import Queue

with open('inp.txt') as f:
    grid = f.read().splitlines()

seen = set()
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dm = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, 1): '>',
    (0, -1): '<'
}

ans = 0
k = 0
regions = defaultdict(set)
regions_dirs = defaultdict(list)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in seen:
            continue
        k += 1

        t = grid[i][j]
        q = Queue()
        q.put((i, j))

        p = 0
        while not q.empty():
            x, y = q.get()

            if (x, y) in seen:
                continue

            seen.add((x, y))
            regions[k].add((x, y))
            p = 0
            for dx, dy in dd:
                if not (0 <= dx + x < len(grid) and 0 <= dy + y < len(grid[0])):
                    continue
                if grid[x + dx][y + dy] == t:
                    q.put((x + dx, y + dy))


for ridx, region in regions.items():
    for x, y in region:
        for dx, dy in dd:
            if (x + dx, y + dy) not in region:
                regions_dirs[ridx].append((x, y, dm[(dx, dy)]))

for ridx, region_dir in regions_dirs.items():
    sides = 0
    for x, y, dir in region_dir:
        if dir in ['^', 'v'] and (x, y + 1, dir) not in region_dir:
            sides += 1
        if dir in ['<', '>'] and (x + 1, y, dir) not in region_dir:
            sides += 1

    ans += (sides * len(regions[ridx]))

print(ans)
