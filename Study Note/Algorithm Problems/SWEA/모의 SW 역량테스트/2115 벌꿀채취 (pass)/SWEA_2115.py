import sys
sys.stdin = open("input.txt", "r")


def max_cost(k, S, cost):
    global cost2
    if k == M:
        if cost > cost2:
            cost2 = cost
        return

    if S + sub[k] <= C:
        max_cost(k + 1, S + sub[k], cost + (sub[k] * sub[k]))
    max_cost(k + 1, S, cost)
    return


T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////
    N, M, C = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        for j in range(N - M + 1):
            cost1 = 0
            # 두 번째 사람
            # 같은 행
            for l in range(j + M, N - M + 1):
                cost2 = 0
                sub = info[i][l: l + M]
                # 해당 부분 배열의 용량 C 이하의 최대 이익
                max_cost(0, 0, 0)
                if cost2 > cost1:
                    cost1 = cost2

            # 다른 행
            for k in range(i + 1, N):
                for l in range(N - M + 1):
                    cost2 = 0
                    sub = info[k][l: l + M]
                    max_cost(0, 0, 0)
                    if cost2 > cost1:
                        cost1 = cost2

            cost2 = 0
            sub = info[i][j: j + M]
            max_cost(0, 0, 0)
            cost1 += cost2

            if cost1 > res:
                res = cost1

    print('#{} {}'.format(test_case, res))





