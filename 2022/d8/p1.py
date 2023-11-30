with open("inp.txt") as f:
    trees = [[int(x) for x in list(t)] for t in f.read().splitlines()]

ans = set()
for i, row in enumerate(trees):
    biggest = -1
    for j in range(len(row)):
        if row[j] > biggest:
            ans.add((i, j))
            biggest = row[j]

    biggest = -1
    for j in range(len(row) - 1, -1, -1):
        if row[j] > biggest:
            ans.add((i, j))
            biggest = row[j]

for j in range(len(trees[0])):
    biggest = -1
    for i in range(len(trees[j])):
        # print(i,j)
        if trees[i][j] > biggest:
            ans.add((i, j))
            biggest = trees[i][j]

    biggest = -1
    for i in range(len(trees[j]) - 1, -1, -1):
        if trees[i][j] > biggest:
            ans.add((i, j))
            biggest = trees[i][j]


print(len(ans))
