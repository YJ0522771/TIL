import sys
sys.stdin = open("input.txt", "r")


def solve(k, prob):
    global res
    global visit
    if k == N:
        if res < prob * 100:
            res = prob * 100
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            temp = prob * P[k][i]
            if temp * 100 > res:
                solve(k + 1, prob * P[k][i])
            visit[i] = False
    return


T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////
    N = int(input())
    P = [list(map(lambda x: x / 100, map(float, input().split()))) for _ in range(N)]
    # print(P)

    res = 0.0
    visit = [False] * N
    solve(0, 1.0)

    print('#%d %.6f' %(test_case, res))
