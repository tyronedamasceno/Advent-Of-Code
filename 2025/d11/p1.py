with open("inp.txt") as f:
    lines = f.read().splitlines()

adj = {}

for line in lines:
    adj[line[:3]] = line[5:].split()


def solve(device):
    if device == "out":
        return 1

    return sum(solve(d) for d in adj[device])


print(solve("you"))
