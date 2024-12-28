with open('inp.txt') as f:
    lines = list(map(int, f.read().splitlines()))


def get_next(sec):
    sec = ((sec * 64) ^ sec) % 16777216
    sec = ((sec // 32) ^ sec) % 16777216
    sec = ((sec * 2048) ^ sec) % 16777216
    return sec


d = {}
print('loop 1')
for i, sec in enumerate(lines):
    d[i] = [(sec % 10, None)]
    for _ in range(2000):
        sec = get_next(sec)
        d[i].append((sec % 10, sec % 10 - d[i][-1][0]))

seq_values = {}
seqs = set()
print('loop 2')
for k, l in d.items():
    seq_values[k] = {}
    for i in range(5, 2002):
        seq = tuple(x[1] for x in l[i - 4:i])
        if seq not in seq_values[k]:
            seqs.add(seq)
            seq_values[k][seq] = d[k][i - 1][0]

ans = -1

print('loop 3')
for seq in seqs:
    lans = 0
    for buyer in d:
        lans += seq_values[buyer].get(seq, 0)
    ans = max(ans, lans)

print(ans)
