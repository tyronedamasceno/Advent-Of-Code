with open('inp.txt') as f:
    rules, line = f.read().split('\n\n')

rules = rules.splitlines()

ans = set()

for rule in rules:
    orig, dest = rule.split(' => ')
    idxs = []
    start = 0
    while (idx := line.find(orig, start)) != -1:
        new = f'{line[:idx]}{dest}{line[idx + len(orig):]}'
        start = idx + 1
        ans.add(new)

print(len(ans))
