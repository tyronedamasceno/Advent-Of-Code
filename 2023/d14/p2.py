with open("inp.txt") as f:
    lines = f.read().split('\n')

grid = [l for l in lines]


def total_load(grid):
    ans = 0
    for idx, line in enumerate(grid):
        ans += (len(grid) - idx) * line.count('O')
    return ans


def transpose(grid):
    grid = [list(r) for r in zip(*grid)]
    return grid


def move(grid, left=True):
    grid = [
        list("#".join(["".join(sorted(k, reverse=left)) for k in "".join(l).split("#")]))
        for l in grid
    ]
    return grid


def north(grid):
    grid = transpose(grid)
    grid = move(grid)
    grid = transpose(grid)
    return grid


def west(grid):
    grid = move(grid)
    return grid


def south(grid):
    grid = grid[::-1]
    grid = transpose(grid)
    grid = move(grid)
    grid = transpose(grid)
    grid = grid[::-1]
    return grid


def east(grid):
    grid = move(grid, left=False)
    return grid


seen = set()
grids = []

while True:
    grid = tuple(grid)
    if grid in seen:
        break
    seen.add(grid)
    grids.append(grid)

    grid = [list(l) for l in grid]

    grid = north(grid)
    grid = west(grid)
    grid = south(grid)
    grid = east(grid)

    grid = [''.join(l) for l in grid]

first_idx = grids.index(grid)
last_grid = grids[(1000000000 - first_idx) % (len(seen) - first_idx) + first_idx]
print(total_load(last_grid))
