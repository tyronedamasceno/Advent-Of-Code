from string import digits

with open("inp.txt") as f:
    lines = f.read().split("\n")

ans = 0
spelled = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in lines:
    numbers = []
    for d in digits:
        idx = line.find(d)
        if idx != -1:
            numbers.append((idx, d))
        idx = line.rfind(d)
        if idx != -1:
            numbers.append((idx, d))
    for d, v in spelled.items():
        idx = line.find(d)
        if idx != -1:
            numbers.append((idx, v))
        idx = line.rfind(d)
        if idx != -1:
            numbers.append((idx, v))

    numbers.sort()
    ans += int(f"{numbers[0][1]}{numbers[-1][1]}")

print(ans)
