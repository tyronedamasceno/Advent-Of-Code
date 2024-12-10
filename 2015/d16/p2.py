with open('inp.txt') as f:
    lines = f.read().splitlines()

mfcsam = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

for idx, line in enumerate(lines):
    props = line[line.find(':') + 2:]
    sue = {}
    for p in props.split(', '):
        k, v = p.split(': ')
        sue[k] = int(v)

    flag = True
    for k, v in sue.items():
        if k in ('cats', 'trees') and v <= mfcsam[k]:
            flag = False
            break
        elif k in ('pomeranians', 'goldfish') and v >= mfcsam[k]:
            flag = False
            break
        elif k not in ('cats', 'trees', 'pomeranians', 'goldfish') and v != mfcsam[k]:
            flag = False
            break
    if flag:
        print(idx + 1)
        print(sue)
        break
