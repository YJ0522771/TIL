import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    V = [0]
    C = [0]
    for _ in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    P = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for v in range(1, K + 1):
            if v >= V[i]:
                P[i][v] = max(P[i - 1][v - V[i]] + C[i], P[i - 1][v])
            else:
                P[i][v] = P[i - 1][v]
    print('#{} {}'.format(test_case, P[N][K]))