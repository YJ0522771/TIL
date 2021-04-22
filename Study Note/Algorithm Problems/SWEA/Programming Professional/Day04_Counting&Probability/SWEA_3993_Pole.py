import sys
sys.stdin = open("input.txt", "r")

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
dp[1][1][1] = 1
for n in range(2, 21):
    for l in range(1, n + 1):
        for r in range(1, n + 1):
            dp[n][l][r] = dp[n - 1][l - 1][r] + dp[n - 1][l][r - 1] + (n - 2) * dp[n - 1][l][r]

# for n in range(1, 21):
#     for l in range(1, n + 1):
#         print(dp[n][l])

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    N, L, R = map(int, input().split())
    print('#{} {}'.format(test_case, dp[N][L][R]))
