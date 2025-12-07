from functools import lru_cache

with open("inp.txt") as f:
    grid = f.read().splitlines()


@lru_cache
def solve(x, y):
    if x == len(grid) - 1:
        return 1

    if grid[x + 1][y] == ".":
        return solve(x + 1, y)

    return solve(x + 1, y - 1) + solve(x + 1, y + 1)


print(solve(0, grid[0].index("S")))
