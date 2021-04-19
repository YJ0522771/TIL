import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    N = int(input())
    image = [[1] * (N + 1)]
    for _ in range(N):
        image.append([1] + list(map(int, list(input()))))
    # print(image)

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # for i in range(N):
    #     dp[0][i] = 1
    #     dp[i][0] = 1

    res = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if image[i][j]:
                continue

            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
            if dp[i][j] > res:
                res = dp[i][j]

    # for i in range(N):
    #     print(dp[i])
    print('#{} {}'.format(test_case, res))