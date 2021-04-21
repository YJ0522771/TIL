import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////
    N = int(input())
    if N == 1:
        print('#{} {}'.format(test_case, 1))
        continue
    elif N == 2:
        print('#{} {}'.format(test_case, 3))
        continue
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    print('#{} {}'.format(test_case, dp[N]))
