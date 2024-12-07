with open('inp.txt') as f:
    lines = f.read().splitlines()


def solve(nums, t, acc):
    if not nums:
        return t == acc

    return solve(nums[1:], t, (acc + nums[0])) or solve(nums[1:], t, (acc * nums[0]))


ans = 0

for l in lines:
    r = int(l.split(':')[0])
    nums = list(map(int, l.split(':')[1][1:].split()))

    if solve(nums[1:], r, nums[0]):
        ans += r

print(ans)
