with open("inp.txt") as f:
    m = [[int(x) for x in line] for line in f.read().split("\n")]


def _is_lower(m, i, j):
    if i > 0 and m[i][j] >= m[i - 1][j]:
        return False
    if j > 0 and m[i][j] >= m[i][j - 1]:
        return False
    if i < len(m) - 1 and m[i][j] >= m[i + 1][j]:
        return False
    if j < len(m[0]) - 1 and m[i][j] >= m[i][j + 1]:
        return False
    return True


ans = 0

for i in range(len(m)):
    for j in range(len(m[0])):
        if _is_lower(m, i, j):
            ans += m[i][j] + 1

print(ans)
