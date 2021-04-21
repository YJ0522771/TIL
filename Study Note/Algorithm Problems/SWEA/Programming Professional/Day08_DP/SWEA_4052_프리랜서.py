import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    N, M = map(int, input().split())

    works = [tuple(map(int, input().split())) for _ in range(N)]
    works.sort(key=lambda x: (x[1]))
    # 인덱스를 1부터 시작하기 위해
    works = [(0, 0, 0)] + works

    before = [0] * (N + 1)
    for i in range(N, 0, -1):
        if works[i][0] == 1:
            before[i] = 0
            continue
        left = 1
        right = N
        while left <= right:
            mid = (left + right) // 2
            if works[mid][1] >= works[i][0]:
                right = mid - 1
            elif works[mid][1] < works[i][0]:
                left = mid + 1
            else:
                break

        if works[mid][1] < works[i][0]:
            before[i] = mid
        else:
            before[i] = mid - 1

    # print(works)
    # print(before)
    # before = [0] + before

    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], dp[before[i]] + works[i][2])

    print('#{} {}'.format(test_case, dp[N]))
