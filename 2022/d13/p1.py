import json


def check_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        if left == right:
            return 0
        return -1

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    for x, y in zip(left, right):
        tmp = check_order(x, y)
        if tmp != 0:
            return tmp

    if len(left) < len(right):
        return 1
    elif len(left) == len(right):
        return 0


with open("inp.txt") as f:
    lines = [json.loads(x) for x in f.read().replace("\n\n", "\n").splitlines()]

k = 0
ans = 0

for i in range(0, len(lines), 2):
    k += 1
    a = lines[i]
    b = lines[i + 1]

    # if k == 4:
    #     breakpoint()
    if check_order(a, b) == 1:
        # print(k)
        ans += k

print(ans)
