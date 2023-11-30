from collections import defaultdict
from queue import Queue
from math import prod


def _get_op_func(operator, value):
    if operator == "+":
        if value == "old":
            return lambda x: x + x
        return lambda x: x + int(value)
    else:
        if value == "old":
            return lambda x: x * x
        return lambda x: x * int(value)


with open("inp.txt") as f:
    lines = f.read().splitlines()

monkeys_begin_lines = [i for i, line in enumerate(lines) if "Monkey " in line]

monkeys_inspection = defaultdict(int)
monkeys_pack = defaultdict(Queue)
monkeys_operation = {}
monkeys_div_test = {}
monkey_true_destination = {}
monkey_false_destination = {}

for mk_idx, monkey_start in enumerate(monkeys_begin_lines):
    _, st_items = lines[monkey_start + 1].split(":")
    for it in st_items.split(","):
        v = int(it.strip())
        monkeys_pack[mk_idx].put(v)

    operator, value = lines[monkey_start + 2][23:].split()
    monkeys_operation[mk_idx] = _get_op_func(operator, value)

    monkeys_div_test[mk_idx] = int(lines[monkey_start + 3][21:])
    monkey_true_destination[mk_idx] = int(lines[monkey_start + 4][29:])
    monkey_false_destination[mk_idx] = int(lines[monkey_start + 5][30:])

rounds = 10000
mod = prod(monkeys_div_test.values())

while rounds:
    rounds -= 1
    for i in range(len(monkeys_begin_lines)):
        while not monkeys_pack[i].empty():
            monkeys_inspection[i] += 1
            item = monkeys_pack[i].get()
            newv = monkeys_operation[i](item)
            newv %= mod
            if newv % monkeys_div_test[i] == 0:
                monkeys_pack[monkey_true_destination[i]].put(newv)
            else:
                monkeys_pack[monkey_false_destination[i]].put(newv)

print(prod(sorted(monkeys_inspection.values(), reverse=True)[:2]))
