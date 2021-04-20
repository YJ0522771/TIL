import sys
sys.stdin = open("input.txt", "r")


def solve(k, cost):
    global res
    global visit
    if k == N:
        if res > cost:
            res = cost
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            new_cost = cost + V[k][i]
            if new_cost < res:
                solve(k + 1, new_cost)
            visit[i] = False
    return


T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    visit = [False] * N
    res = 1000000
    solve(0, 0)
    print('#{} {}'.format(test_case, res))
