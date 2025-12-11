from collections import defaultdict

with open("inp.txt") as f:
    lines = f.read().splitlines()

adj = {}

for line in lines:
    adj[line[:3]] = line[5:].split()

memo = defaultdict(int)


def solve(device, dac=False, fft=False):
    if (device, dac, fft) in memo:
        return memo[(device, dac, fft)]

    if device == "out" and dac and fft:
        return 1
    elif device == "out":
        return 0

    ndac = dac or device == "dac"
    nfft = fft or device == "fft"

    memo[(device, dac, fft)] = sum(solve(d, ndac, nfft) for d in adj[device])
    return memo[(device, dac, fft)]


print(solve("svr"))
