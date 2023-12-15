from collections import defaultdict

with open("inp.txt") as f:
    lines = f.read().split('\n')


def get_box(seq):
    tmp = 0
    for c in seq:
        tmp += ord(c)
        tmp *= 17
        tmp %= 256
    return tmp


boxes = defaultdict(list)
boxes_labels = defaultdict(list)
for seq in lines[0].split(','):
    if '-' in seq:
        label = seq[:-1]
        box = get_box(label)
        if label in boxes_labels[box]:
            idx = boxes_labels[box].index(label)
            boxes[box].pop(idx)
            boxes_labels[box].pop(idx)
    else:
        label, k = seq.split('=')
        box = get_box(label)
        if label in boxes_labels[box]:
            idx = boxes_labels[box].index(label)
            boxes[box][idx] = (label, k)
        else:
            boxes[box].append((label, k))
            boxes_labels[box].append(label)

ans = 0

for box, lenses in boxes.items():
    for idx, lens in enumerate(lenses):
        ans += ((box + 1) * (idx + 1) * int(lens[1]))

print(ans)
