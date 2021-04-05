N, K = map(int, input().split())
res = 0
for i in range(1, N + 1):
    res = (res + K) % i

print(res + 1)