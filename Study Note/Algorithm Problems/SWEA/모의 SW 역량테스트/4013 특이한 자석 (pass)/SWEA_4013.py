import sys
sys.stdin = open("input.txt", "r")

N, M = 4, 8
left, right = 6, 2
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////
    K = int(input())
    # N = 0, S = 1
    magnet = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(K):
        n, d = map(int, input().split())
        n -= 1

        NS = [False] * N
        for i in range(1, N):
            if n + i < N and magnet[n + i - 1][right] != magnet[n + i][left]:
                NS[n + i] = True
            if n - i >= 0 and magnet[n - i][right] != magnet[n - i + 1][left]:
                NS[n - i] = True

        temp = [0] * M
        for i in range(M):
            temp[(i + d) % M] = magnet[n][i]
        magnet[n] = list(temp)

        # 0 : 오른쪽, 1 : 왼쪽
        # 해당 방향으로 더 돌릴 가능성이 있는 지
        # 3번째 것을 돌리고 NS가 T F F T라면,
        # 첫 번째 자석은 T이지만 두 번째가 돌아기지 않으므로 돌리지 않는다.
        dd = [True] * 2
        for i in range(1, N):
            t = d * (-1)**i
            if dd[0] and n + i < N and NS[n + i]:
                for j in range(M):
                    temp[(j + t) % M] = magnet[n + i][j]
                magnet[n + i] = list(temp)
            else:
                dd[0] = False

            if dd[1] and n - i >= 0 and NS[n - i]:
                for j in range(M):
                    temp[(j + t) % M] = magnet[n - i][j]
                magnet[n - i] = list(temp)
            else:
                dd[1] = False
        # for i in range(N):
        #     print(magnet[i])
        # print()

    res = 0
    for i in range(N):
        # print(magnet[i])
        res += magnet[i][0] * 2**i

    print('#{} {}'.format(test_case, res))
