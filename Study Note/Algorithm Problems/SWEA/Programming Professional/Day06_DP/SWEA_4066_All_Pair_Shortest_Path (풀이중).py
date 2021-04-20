import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////
    N, M = map(int, input().split())
    adj_k_1 = [[1000000000] * (N + 1) for _ in range(N + 1)]
    adj_k = [[1000000000] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        adj_k_1[a][b] = c
    for i in range(N + 1):
        adj_k_1[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    adj_k[i][j] = 0
                    continue
                if i != k and j != k:
                    adj_k[i][j] = min(adj_k_1[i][k] + adj_k_1[k][j], adj_k_1[i][j])
                else:
                    adj_k[i][j] = adj_k_1[i][j]

        # print(adj_k_1)
        for i in range(N + 1):
            adj_k_1[i] = list(adj_k[i])

        # print(adj_k)
        # print()

    # for i in range(N + 1):
    #     print(adj[N][i])

    print('#{}'.format(test_case), end='')
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(' {}'.format(-1 if adj_k[i][j] == 1000000000 else adj_k[i][j]), end='')
    print()


