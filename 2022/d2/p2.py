with open("inp.txt") as f:
    lines = [x.split(" ") for x in f.read().split("\n")]

points = {
    "X": 1,  # rock
    "Y": 2,  # paper
    "Z": 3,  # scissors
}

elf_wins = {
    "C": "X",
    "A": "Y",
    "B": "Z",
}
elf_draws = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
elf_loses = {
    "B": "X",
    "C": "Y",
    "A": "Z",
}

ans = 0

for op, res in lines:
    if res == "Z":
        ans += 6
        elf_play = elf_wins[op]
    if res == "Y":
        ans += 3
        elf_play = elf_draws[op]
    if res == "X":
        elf_play = elf_loses[op]

    ans += points[elf_play]


print(ans)
