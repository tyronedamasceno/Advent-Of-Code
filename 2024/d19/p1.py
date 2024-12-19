from functools import lru_cache

with open('inp.txt') as f:
    towels, designs = f.read().split('\n\n')
    towels = set(towels.split(', '))
    designs = designs.splitlines()


@lru_cache
def solve(design):
    if design == '':
        return True
    if design in towels:
        return True

    return any(
        design[:i] in towels and solve(design[i:])
        for i in range(len(design))
    )


ans = 0
for design in designs:
    if solve(design):
        ans += 1

print(ans)
