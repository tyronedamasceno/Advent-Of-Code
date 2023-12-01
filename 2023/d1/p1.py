from string import digits

with open("inp.txt") as f:
    lines = f.read().split("\n")

ans = 0

for line in lines:
    tmp = ""
    for i in line:
        if i in digits:
            tmp += i
            break
    for i in line[::-1]:
        if i in digits:
            tmp += i
            break
    ans += int(tmp)

print(ans)
