N = int(input())
info = [[0, 0, 0]]
for _ in range(N):
    R, G, B = map(int, input().split())
    info.append([R, G, B])

dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    if dp[i - 1][1] < dp[i - 1][2]:
        dp[i][0] = info[i][0] + dp[i - 1][1]
    else:
        dp[i][0] = info[i][0] + dp[i - 1][2]

    if dp[i - 1][0] < dp[i - 1][2]:
        dp[i][1] = info[i][1] + dp[i - 1][0]
    else:
        dp[i][1] = info[i][1] + dp[i - 1][2]

    if dp[i - 1][1] < dp[i - 1][0]:
        dp[i][2] = info[i][2] + dp[i - 1][1]
    else:
        dp[i][2] = info[i][2] + dp[i - 1][0]

print(min(dp[N]))