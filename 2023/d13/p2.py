with open("inp.txt") as f:
    lines = [[list(pattern) for pattern in chunk.split('\n')]
             for chunk in f.read().split('\n\n')]


def reflection_h(pattern, old, v=False):
    for i in range(1, len(pattern)):
        flag = True
        for x, y in zip(pattern[:i][::-1], pattern[i:]):
            if x != y:
                flag = False
                break
        if flag:
            if (i * 100) != old and not v:
                return i * 100
            if i != old and v:
                return i


def reflection_v(pattern, old):
    pattern_columns = [[row[idx] for row in pattern] for idx in range(len(pattern[0]))]
    return reflection_h(pattern_columns, old, v=True)


def reflection(pattern, old=0):
    return reflection_h(pattern, old) or reflection_v(pattern, old)


def flip(c):
    return '#' if c == '.' else '.'


def reflection_clean(pattern, old):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            pattern[i][j] = flip(pattern[i][j])
            tmp = reflection(pattern, old)
            if tmp:
                return tmp
            pattern[i][j] = flip(pattern[i][j])


ans = 0
for pattern in lines:
    tmp = reflection(pattern)
    ans += reflection_clean(pattern, tmp)
print(ans)
