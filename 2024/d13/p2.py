from tqdm import tqdm
from queue import Queue

with open('inp.txt') as f:
    combos = f.read().split('\n\n')

ans = 0

for combo in tqdm(combos):
    ba, bb, prize = combo.splitlines()
    bax, bay = ba[10:].split(', ')
    bax, bay = int(bax[2:]), int(bay[2:])

    bbx, bby = bb[10:].split(', ')
    bbx, bby = int(bbx[2:]), int(bby[2:])

    px, py = prize[7:].split(', ')
    px, py = int(px[2:]), int(py[2:])
    px += 10000000000000
    py += 10000000000000

    break

    qu = Queue()
    qu.put((bax, bay, 3))
    qu.put((bbx, bby, 1))

    lans = float('inf')
    seen = set()

    while not qu.empty():
        x, y, k = qu.get()
        if ((x, y, k)) in seen:
            continue
        seen.add((x, y, k))
        if (x, y) == (px, py):
            lans = min(lans, k)
            continue
        if k > lans:
            continue
        if x > px or y > py:
            continue

        qu.put((x + bax, y + bay, k + 3))
        qu.put((x + bbx, y + bby, k + 1))

    if lans != float('inf'):
        ans += lans

print(ans)
