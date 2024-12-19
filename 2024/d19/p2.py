from functools import lru_cache

with open('inp.txt') as f:
    towels, designs = f.read().split('\n\n')
    towels = set(towels.split(', '))
    designs = designs.splitlines()


@lru_cache
def solve(design):
    if design == '':
        return 1

    tmp = 0
    for i in range(len(design) + 1):
        if design[:i] in towels:
            tmp += solve(design[i:])

    return tmp


ans = 0
for design in designs:
    ans += solve(design)

print(ans)
