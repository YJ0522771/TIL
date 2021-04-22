import sys
sys.stdin = open("input.txt", "r")

# Floyd-Warshall : O(N^3)라서 시간 초과

MAX = 10000000
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    N, E = map(int, input().split())
    adj_k_1 = [[MAX] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_k_1[s][e] = w
    adj_k = [[MAX] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        adj_k_1[i][i] = 0

    for k in range(N + 1):
        for i in range(N + 1):
            for j in range(N + 1):
                if i == j:
                    adj_k[i][j] = 0
                    continue
                if i != k and j != k:
                    if adj_k_1[i][k] + adj_k_1[k][j] < adj_k_1[i][j]:
                        adj_k[i][j] = adj_k_1[i][k] + adj_k_1[k][j]
                    else:
                        adj_k[i][j] = adj_k_1[i][j]
                else:
                    adj_k[i][j] = adj_k_1[i][j]

        # print(adj_k_1)
        for i in range(N + 1):
            adj_k_1[i] = list(adj_k[i])

    # print(adj_k)
    print('#{} {}'.format(test_case, adj_k[0][N]))