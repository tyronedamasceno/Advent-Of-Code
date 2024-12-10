def next_code(k):
    return (k * 252533) % 33554393


def next_position(i, j):
    if i == 1:
        return (j + 1, 1)

    return (i - 1, j + 1)


p = 2947, 3029

i = 1
j = 1

code = 20151125

while True:
    i, j = next_position(i, j)
    code = next_code(code)
    if (i, j) == p:
        break

print(code)
