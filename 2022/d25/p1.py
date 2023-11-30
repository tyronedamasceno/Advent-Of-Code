# 1 5 25 125 625 3125 15625 78125


def snafu_to_int(snafu: str) -> int:
    conversion_base = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    exp = len(snafu) - 1
    tmp = 0
    for x in snafu:
        tmp += (5**exp) * conversion_base[x]
        exp -= 1
    return tmp


def int_to_snafu(integer: int) -> str:
    conversion_base = "=-012"
    tmp = ""

    while integer:
        integer, mod = divmod(integer + 2, 5)
        tmp += conversion_base[mod]

    return tmp[::-1]


with open("inp.txt") as f:
    snafus = f.read().split("\n")

int_sum = sum(snafu_to_int(snafu) for snafu in snafus)

print(int_sum)

ans = int_to_snafu(int_sum)

print(ans)
