from functools import cmp_to_key
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
    return -1


with open("inp.txt") as f:
    lines = [json.loads(x) for x in f.read().replace("\n\n", "\n").splitlines()]

lines.append([[2]])
lines.append([[6]])

lines = sorted(lines, key=cmp_to_key(check_order), reverse=True)

print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))
