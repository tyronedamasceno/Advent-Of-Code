with open('inp.txt') as f:
    combos = f.read().split('\n\n')

ans = 0

for combo in combos:
    ba, bb, prize = combo.splitlines()
    bax, bay = ba[10:].split(', ')
    bax, bay = int(bax[2:]), int(bay[2:])

    bbx, bby = bb[10:].split(', ')
    bbx, bby = int(bbx[2:]), int(bby[2:])

    px, py = prize[7:].split(', ')
    px, py = int(px[2:]), int(py[2:])
    px += 10000000000000
    py += 10000000000000

    b2 = ((-bay / bax) * px + py) / ((-bay / bax) * bbx + bby)
    b1 = (px - (b2 * bbx)) / bax

    b1 = round(b1)
    b2 = round(b2)

    if b1 * bax + b2 * bbx != px or b1 * bay + b2 * bby != py:
        continue

    ans += b1 * 3 + b2

print(ans)
