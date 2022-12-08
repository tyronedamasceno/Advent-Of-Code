with open('inp.txt') as f:
    trees = [[int(x) for x in list(t)] for t in f.read().splitlines()]

ans = -1

def _find_score(i, j, trees):
    score = 1
    cur = trees[i][j]

    # down
    local_score = 0
    for x in range(i+1, len(trees)):
        local_score += 1
        if trees[x][j] >= cur:
            break
    score *= local_score

    # right
    local_score = 0
    for y in range(j+1, len(trees[0])):
        local_score += 1
        if trees[i][y] >= cur:
            break
    score *= local_score

    # up
    local_score = 0
    for x in range(i-1, -1, -1):
        local_score += 1
        if trees[x][j] >= cur:
            break
    score *= local_score

    # left
    local_score = 0
    for y in range(j-1, -1, -1):
        local_score += 1
        if trees[i][y] >= cur:
            break
    score *= local_score

    return score

for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        ans = max(ans, _find_score(i, j, trees))

print(ans)
