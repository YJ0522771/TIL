import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    str1, str2 = input().split()
    N, M = len(str1), len(str2)
    case = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if str1[i - 1] == str2[j - 1]:
                case[i][j] = case[i - 1][j - 1] + 1
            else:
                case[i][j] = case[i - 1][j] if case[i - 1][j] > case[i][j - 1] else case[i][j - 1]
    print('#{} {}'.format(test_case, case[N][M]))