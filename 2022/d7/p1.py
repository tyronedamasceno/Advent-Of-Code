from collections import defaultdict
import queue

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

def _get_tree_size(root):
    q = queue.Queue()
    ans = 0
    q.put(root)
    while not q.empty():
        t = q.get()
        ans += dsize[t]
        for child in dchild[t]:
            q.put(child)
    return ans

dans = {}
for d in dparent.keys():
    dans[d] = _get_tree_size(d)

ans = 0
for sz in dans.values():
    if sz <= 100000:
        ans += sz

print(ans)
