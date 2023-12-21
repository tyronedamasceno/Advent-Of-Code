from copy import deepcopy

with open("inp.txt") as f:
    lines = f.read().split('\n')

workflows = {}
for workflow in lines[:lines.index('')]:
    name, rules = workflow[:-1].split('{')
    workflows[name] = rules.split(',')


def solve(flow, ranges):
    if flow == 'R':
        return 0

    if flow == 'A':
        k = 1
        for v in ranges.values():
            k *= len(v)
        return k

    tmp = 0
    for rule in workflows[flow]:
        if ':' not in rule:
            tmp += solve(rule, ranges)
            continue

        check, nxt = rule.split(':')
        if '<' in check:
            part, value = check.split('<')
            good_range = range(ranges[part].start, int(value))
            bad_range = range(int(value), ranges[part].stop)
            goods = deepcopy(ranges)
            goods[part] = good_range
            ranges[part] = bad_range
            tmp += solve(nxt, goods)
        elif '>' in check:
            part, value = check.split('>')
            good_range = range(int(value) + 1, ranges[part].stop)
            bad_range = range(ranges[part].start, int(value) + 1)
            goods = deepcopy(ranges)
            goods[part] = good_range
            ranges[part] = bad_range
            tmp += solve(nxt, goods)

    return tmp


ranges = {v: range(1, 4001) for v in ['x', 'm', 'a', 's']}
ans = solve('in', ranges)
print(ans)
