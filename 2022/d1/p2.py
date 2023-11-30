with open("inp.txt") as f:
    cals_per_elf = f.read().split("\n\n")

cals_per_elf = [sum(int(x) for x in elf.split("\n")) for elf in cals_per_elf]

ans = sum(sorted(cals_per_elf, reverse=True)[:3])

print(ans)
