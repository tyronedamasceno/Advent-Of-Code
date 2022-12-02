with open('inp.txt') as f:
    lines = [x.split(' ') for x in f.read().split('\n')]

points = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3,  # scissors
}


elf_wins = {('X', 'C'), ('Y', 'A'), ('Z', 'B')}
elf_draws = {('X', 'A'), ('Y', 'B'), ('Z', 'C')}

ans = 0

for op, elf in lines:
    ans += points[elf]

    if (elf, op) in elf_wins:
        ans += 6

    if (elf, op) in elf_draws:
        ans += 3

print(ans)
