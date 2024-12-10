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

    if all(item in mfcsam.items() for item in sue.items()):
        print(idx + 1)
        print(sue)
        break
