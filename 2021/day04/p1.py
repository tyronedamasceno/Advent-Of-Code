def _get_columns(lines):
    return [
        [lines[j][i] for j in range(5)] for i in range(5)
    ]

with open('inp.txt') as f:
    draw = [int(x) for x in f.readline()[:-1].split(',')]
    l = [
        [int(k) for k in x.split()]
        for x in f.read().split('\n') if x
    ]

boards = {
    i // 5: l[i:i+5] for i in range(0, len(l), 5)
}

boards_sets = {
    k: [
        set(line) for line in lines
    ] + [set(column) for column in _get_columns(lines)]
    for k, lines in boards.items()
}

winner = None
found = None

for d in draw:
    if winner:
        break
    for k, board in boards_sets.items():
        if winner:
            break
        for x in board:
            x.discard(d)
            if len(x) == 0:
                winner = k
                found = d

winner_board_sets = boards_sets[winner]
remain = set()
for s in winner_board_sets:
    remain |= s
remain.discard(found)

print(sum(remain) * found)
