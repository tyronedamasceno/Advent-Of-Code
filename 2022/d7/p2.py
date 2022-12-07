from collections import defaultdict
from functools import lru_cache

with open('inp.txt') as f:
    lines = f.read().splitlines()


dparent = {}
dsize = defaultdict(int)
dchild = defaultdict(set)
cur_dir = ''

for line in lines:
    if line[0] == "$":
        if line == "$ ls":
            continue
        _, _, dirname = line.split()
        if dirname == "..":
            cur_dir = dparent[cur_dir]
            continue
        if dirname == '/':
            cur_dir = '/'
            dparent[cur_dir] = None
        else:
            tmp = f'{cur_dir}/{dirname}'
            dparent[tmp] = cur_dir
            cur_dir = tmp
    else:
        a, b = line.split()
        if a == 'dir':
            dchild[cur_dir].add(f'{cur_dir}/{b}')
        else:
            dsize[cur_dir] += int(a)

@lru_cache
def _get_tree_size(root):
    return dsize[root] + sum(_get_tree_size(child) for child in dchild[root])


dans = {}
for d in dparent.keys():
    dans[d] = _get_tree_size(d)


total = 70000000
inuse = dans['/']
freespace = total - inuse
required = 30000000
least = required - freespace

for k in sorted(dans.values()):
    if k >= least:
        print(k)
        break

