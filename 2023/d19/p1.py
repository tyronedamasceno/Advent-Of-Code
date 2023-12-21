with open("inp.txt") as f:
    lines = f.read().split('\n')

workflows = {}
for workflow in lines[:lines.index('')]:
    name, rules = workflow[:-1].split('{')
    workflows[name] = rules.split(',')

parts = []
for part in lines[lines.index('') + 1:]:
    parts.append({
        x.split('=')[0]: int(x.split('=')[1])
        for x in part[1:-1].split(',')
    })


def solve(part, workflow):
    if workflow == 'A':
        return True
    if workflow == 'R':
        return False

    for rule in workflows[workflow]:
        if ':' not in rule:
            return solve(part, rule)
        check, nxt = rule.split(':')
        if '<' in check:
            p, v = check.split('<')
            if part[p] < int(v):
                return solve(part, nxt)
        if '>' in check:
            p, v = check.split('>')
            if part[p] > int(v):
                return solve(part, nxt)


ans = 0
for part in parts:
    if solve(part, 'in'):
        ans += sum(part.values())
print(ans)
