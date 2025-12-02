with open("inp.txt") as f:
    line = f.read().split(',')

def is_invalid(k):
    k = str(k)
    for i in range(1, len(k) // 2 + 1):
        if len(k) % i != 0:
            continue
        s = set()
        for x in range(0, len(k), i):
            s.add(k[x:x+i])
        if len(s) == 1:
            return True
    return False

ans = 0
for x in line:
    a, b = map(int, x.split('-'))

    for k in range(a, b+1):
        if is_invalid(k):
            ans += k

print(ans)
