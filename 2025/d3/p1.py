with open("inp.txt") as f:
    lines = f.read().splitlines()


def get_max(bank, last=False):
    for dig in '987654321':
        idx = bank.find(dig)
        if idx == -1:
            continue
        if idx == len(bank) - 1 and not last:
            continue

        return idx

ans = 0

for bank in lines:
    i1 = get_max(bank)
    i2 = get_max(bank[i1+1:], last=True)

    ans += int(f'{bank[i1]}{bank[i1+1+i2]}')

print(ans)
