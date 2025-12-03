with open("inp.txt") as f:
    lines = f.read().splitlines()


def get_max(bank, offset):
    for dig in '987654321':
        idx = bank.find(dig)
        if idx == -1:
            continue
        if idx > len(bank) - offset:
            continue

        return idx

ans = 0

for bank in lines:
    tmp = ''
    prev = 0
    i = get_max(bank, 12)
    tmp += bank[i]
    for k in range(11, 0, -1):
        prev += i + 1
        i = get_max(bank[prev:], k)
        tmp += bank[prev+i]

    ans += int(tmp)

print(ans)
