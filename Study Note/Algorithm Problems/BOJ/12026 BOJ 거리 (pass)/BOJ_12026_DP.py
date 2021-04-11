import sys
sys.stdin = open("input.txt", "r")


dic = {'B': [], 'O': [], 'J': []}
BOJ = 'BOJ'

N = int(input())
road = list(input())

for i in range(N):
    dic[road[i]].append(i)

dp = [0] * N
before = [-1] * N
for i in range(1, N):
    c = BOJ[(BOJ.index(road[i]) - 1) % 3]
    m = 1000001
    k = -1
    for j in dic[c]:
        if j > i:
            break
        # 시작점에서 올 수 없는 지점은 거르기.
        if j != 0 and before[j] == -1:
            continue
        temp = dp[j] + (i - j)**2
        if temp < m:
            m = temp
            k = j
    if m != 1000001:
        dp[i] = m
        before[i] = k

print(dp[N - 1] if dp[N - 1] else -1)



