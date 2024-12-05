from collections import defaultdict
import random
from tqdm import tqdm

with open('inp.txt') as f:
    lines = f.read().split('\n')

k = lines.index('')
rules = lines[:k]
updates = [list(map(int, l.split(','))) for l in lines[k + 1:]]

tmp = defaultdict(set)

for rule in rules:
    a, b = map(int, rule.split('|'))
    tmp[a].add(b)


rules = tmp

wrongs = []


def check_correct_order(upd):
    seen = set()
    for x in upd:
        if seen & rules[x]:
            return False
        seen.add(x)
    return True


for upd in updates:
    if not check_correct_order(upd):
        wrongs.append(upd)

ans = 0
for upd in tqdm(wrongs):
    while not check_correct_order(upd):
        random.shuffle(upd)

    ans += upd[len(upd) // 2]

print(ans)
