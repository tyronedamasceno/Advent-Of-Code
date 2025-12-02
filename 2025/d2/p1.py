with open("inp.txt") as f:
    line = f.read().split(',')

ans = 0
for x in line:
    a, b = map(int, x.split('-'))
    
    for k in range(a, b+1):
        k = str(k)
        if len(k) % 2 == 0 and k[:len(k)//2] == k[len(k)//2:]:
            ans += int(k)

print(ans)
