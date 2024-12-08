import string

with open('inp.txt') as f:
    lines = f.read().splitlines()

ans = 0
for line in lines:
    vowels = 0
    for v in 'aeiou':
        vowels += line.count(v)
    if vowels < 3:
        continue

    if any(p in line for p in ['ab', 'cd', 'pq', 'xy']):
        continue

    for l in string.ascii_lowercase:
        if l + l in line:
            ans += 1
            break

print(ans)
