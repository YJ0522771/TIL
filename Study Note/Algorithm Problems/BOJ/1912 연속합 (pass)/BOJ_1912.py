N = int(input())
nums = list(map(int, input().split()))

res = nums[0]
for i in range(1, N):
    if nums[i - 1] > 0 and nums[i] + nums[i - 1] > 0:
        nums[i] += nums[i - 1]
    if res < nums[i]:
        res = nums[i]
print(res)