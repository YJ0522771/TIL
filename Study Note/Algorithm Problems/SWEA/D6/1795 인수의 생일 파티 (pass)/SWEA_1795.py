import sys
sys.stdin = open("input.txt", "r")

MAX = 1000000
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////
    N, M, X = map(int, input().split())
    adj = [[[MAX] * (N + 1) for _ in range(N + 1)] for _ in range(2)]

    for i in range(N + 1):
        adj[0][i][i] = 0
        adj[1][i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[0][x][y] = c
        adj[1][y][x] = c

    D = [[MAX] * (N + 1) for _ in range(2)]
    visit = [[False] * (N + 1) for _ in range(2)]

    for r in range(2):
        D[r][X] = 0
        visit[r][X] = True
        for i in range(1, N + 1):
            D[r][i] = adj[r][X][i]

        count = 1
        while count < N:
            mm = MAX
            e = -1
            for i in range(1, N + 1):
                if not visit[r][i] and mm > D[r][i]:
                    mm = D[r][i]
                    e = i

            visit[r][e] = True
            count += 1
            for i in range(1, N + 1):
                if not visit[r][i] and D[r][i] > mm + adj[r][e][i]:
                    D[r][i] = mm + adj[r][e][i]

    res = 0
    for i in range(1, N + 1):
        if res < D[0][i] + D[1][i]:
            res = D[0][i] + D[1][i]

    print('#{} {}'.format(test_case, res))

