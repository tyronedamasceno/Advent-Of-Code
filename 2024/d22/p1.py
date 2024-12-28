with open('inp.txt') as f:
    lines = list(map(int, f.read().splitlines()))


def get_next(sec):
    sec = ((sec * 64) ^ sec) % 16777216
    sec = ((sec // 32) ^ sec) % 16777216
    sec = ((sec * 2048) ^ sec) % 16777216
    return sec


ans = 0
for buyer in lines:
    for _ in range(2000):
        buyer = get_next(buyer)
    ans += buyer

print(ans)
