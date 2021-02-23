import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    nums = [list(map(int, list(input()))) for _ in range(N)]
    M = N // 2
    res = 0
    for i in range(M):
        for j in range(M - i, M + i + 1):
            res += nums[i][j]
            res += nums[N - 1 - i][j]
    res += sum(nums[M])

    print('#{} {}'.format(test_case, res))
