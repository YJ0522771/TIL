import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    string1 = input()
    string2 = input()

    dp = [[0] * (len(string1) + 1) for _ in range(len(string2) + 1)]
    for i in range(1, len(string2) + 1):
        for j in range(1, len(string1) + 1):
            if string1[j - 1] == string2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for i in range(1, len(string2) + 1):
        print(dp[i])

    print('#{} {}'.format(test_case, dp[len(string2)][len(string1)]))
