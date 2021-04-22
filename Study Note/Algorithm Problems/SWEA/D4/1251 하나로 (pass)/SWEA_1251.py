import sys
sys.stdin = open("input.txt", "r")

MAX = 1000000000000
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())
    adj = [[MAX] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            adj[i][j] = adj[j][i] = ((xs[i] - xs[j])**2 + (ys[i] - ys[j])**2) * E

    visit = [False] * N
    D = [MAX] * N

    visit[0] = True
    D[0] = 0
    for i in range(1, N):
        D[i] = adj[0][i]

    count = 0
    res = 0
    while count < N - 1:
        # 최소 간선 찾기
        mm = MAX
        e = -1
        for i in range(N):
            if not visit[i] and D[i] < mm:
                mm = D[i]
                e = i

        visit[e] = True
        count += 1
        res += mm
        for i in range(N):
            if not visit[i] and D[i] > adj[e][i]:
                D[i] = adj[e][i]
        # print(e, D)

    res = int(round(res, 0))
    print('#{} {}'.format(test_case, res))