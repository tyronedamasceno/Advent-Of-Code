from functools import lru_cache

with open('inp.txt') as f:
    line = f.read()


@lru_cache(maxsize=None)
def solve(stone, steps):
    if steps == 0:
        return 1

    if stone == 0:
        return solve(1, steps - 1)

    if len(str(stone)) % 2 == 0:
        sst = str(stone)
        a, b = sst[:len(sst) // 2], sst[len(sst) // 2:]
        return solve(int(a), steps - 1) + solve(int(b), steps - 1)

    return solve(stone * 2024, steps - 1)


print(sum(solve(s, 75) for s in map(int, line.split())))
