N = int(input())

res = 0
for i in range(1, N):
    K = i
    temp = i
    while temp != 0:
        K += temp % 10
        temp //= 10
    if K == N:
        res = i
        break
print(res)