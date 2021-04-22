import sys
sys.stdin = open("input.txt", "r")

# Dijkstra

MAX = 10000000
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    N, E = map(int, input().split())
    adj = [[MAX] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    D = [MAX] * (N + 1)
    visit = [False] * (N + 1)
    # 시작 정점 세팅
    visit[0] = True
    D[0] = 0
    for i in range(1, N + 1):
        D[i] = adj[0][i]

    count = 1
    while count < N + 1:
        mm = MAX
        e = -1
        for i in range(N + 1):
            if not visit[i] and mm > D[i]:
                mm = D[i]
                e = i

        visit[e] = True
        count += 1

        for i in range(1, N + 1):
            if not visit[i] and D[i] > D[e] + adj[e][i]:
                D[i] = D[e] + adj[e][i]

    print('#{} {}'.format(test_case, D[N]))

