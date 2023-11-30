with open("inp.txt") as f:
    cals_per_elf = f.read().split("\n\n")

ans = float("-inf")

for elf in cals_per_elf:
    ans = max(ans, sum(int(x) for x in elf.split("\n")))

print(ans)
