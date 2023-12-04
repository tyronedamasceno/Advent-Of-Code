with open("inp2.txt") as f:
    lines = f.read().split('\n')

ans = 0

for line in lines:
    _, numbers = line.split(':')
    winner, ours = numbers.split('|')
    ws = set(winner.split())
    os = set(ours.split())
    matches = ws & os
    if matches:
        ans += 2 ** (len(matches) - 1)

print(ans)
