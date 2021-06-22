N = int(input())
if N < 5:
    if N == 3:
        print(1)
    else:
        print(-1)
else:
    dp = [0] * (N + 1)
    dp[3] = 1
    dp[5] = 1
    for i in range(6, N + 1):
        if dp[i - 3] and dp[i - 5]:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1
        elif dp[i - 3]:
            dp[i] = dp[i - 3] + 1
        elif dp[i - 5]:
            dp[i] = dp[i - 5] + 1
    if dp[N]:
        print(dp[N])
    else:
        print(-1)