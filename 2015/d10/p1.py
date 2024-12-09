with open('inp.txt') as f:
    line = f.read()


def count_and_say(s):
    ans = ''

    cur = s[0]
    count = 1

    for k in s[1:]:
        if k == cur:
            count += 1
            continue

        ans += str(count)
        ans += cur
        cur = k
        count = 1

    ans += str(count)
    ans += cur

    return ans


for _ in range(40):
    line = count_and_say(line)

print(len(line))
