N = int(input())
nums = list(map(int, input().split()))
temp = 0
res = -1001
for i in range(N):
    temp += nums[i]
    if res < temp:
        res = temp
    if temp < 0:
        temp = 0
print(res)