N = int(input())
info = []
for _ in range(N):
    t = input()
    if len(t) > 1:
        info.append(list(map(int, t.split())))
    else:
        info.append([int(t)])

dp = [[0] * N for _ in range(N)]
dp[0][0] = info[0][0]
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][0] = dp[i - 1][0] + info[i][0]
        elif j == i:
            dp[i][i] = dp[i - 1][i - 1] + info[i][i]
        else:
            if dp[i - 1][j - 1] > dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j - 1] + info[i][j]
            else:
                dp[i][j] = dp[i - 1][j] + info[i][j]

print(max(dp[N - 1]))