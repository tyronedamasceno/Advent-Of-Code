with open("inp.txt") as f:
    lines = f.read().split("\n")

monkey_values = {}
monkey_ops = {}
unknown = set()


def perform_op(va, op, vb):
    match op:
        case "+":
            return va + vb
        case "*":
            return va * vb
        case "-":
            return va - vb
        case "/":
            return va / vb


def solve(m, ma, op, mb):
    if ma in unknown:
        solve(ma, *monkey_ops[ma])
        unknown.remove(ma)
    if mb in unknown:
        solve(mb, *monkey_ops[mb])
        unknown.remove(mb)

    monkey_values[m] = perform_op(monkey_values[ma], op, monkey_values[mb])
    return monkey_values[m]


for line in lines:
    monkey, job = line.split(":")
    job = job.strip()
    if " " not in job:
        monkey_values[monkey] = int(job)
        continue

    unknown.add(monkey)
    monkey_a, op, monkey_b = job.split(" ")
    monkey_ops[monkey] = (monkey_a, op, monkey_b)

print(solve("root", *monkey_ops["root"]))
