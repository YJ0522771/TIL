import sys
sys.stdin = open("input.txt", "r")

# Prim

MAX = 1000000000
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    V, E = map(int, input().split())
    adj = [[MAX] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        adj[a][b] = w
        adj[b][a] = w
    D = [MAX] * (V + 1)
    visit = [False] * (V + 1)

    # 0번을 시작점으로
    D[0] = 0
    visit[0] = True
    for i in range(1, V + 1):
        D[i] = adj[0][i]

    count = 0
    res = 0
    while count < V:
        mm = MAX
        e = -1
        for i in range(V + 1):
            if not visit[i] and mm > D[i]:
                mm = D[i]
                e = i

        visit[e] = True
        count += 1
        res += mm

        # 최소 경로 갱신
        for i in range(V + 1):
            if not visit[i] and D[i] > adj[e][i]:
                D[i] = adj[e][i]

    print('#{} {}'.format(test_case, res))

