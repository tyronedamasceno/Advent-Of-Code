from string import ascii_lowercase

with open("inp.txt") as f:
    lines = f.read().split("\n")
    lines = [(line[: len(line) // 2], line[len(line) // 2:]) for line in lines]

ans = 0
for a, b in lines:
    k = (set(a) & set(b)).pop()
    if k in ascii_lowercase:
        ans += ord(k) - ord("a") + 1
    else:
        ans += ord(k) - ord("A") + 27

print(ans)
