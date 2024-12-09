def check(s):
    for i in range(len(s) - 2):
        if ord(s[i]) + 1 == ord(s[i + 1]) and ord(s[i]) + 2 == ord(s[i + 2]):
            break
    else:
        return False

    if any(l in s for l in ('i', 'o', 'l')):
        return False

    overlaps = 0
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            overlaps += 1
            i += 1
        i += 1

    if overlaps < 2:
        return False

    return True


def incr(s):
    s_list = list(s)
    i = len(s_list) - 1

    while i >= 0:
        if s_list[i] == 'z':
            s_list[i] = 'a'
            i -= 1
        else:
            s_list[i] = chr(ord(s_list[i]) + 1)
            break

    return ''.join(s_list)


with open('inp.txt') as f:
    line = f.read()

while True:
    line = incr(line)
    if check(line):
        print(line)
        break
