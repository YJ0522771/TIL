import sys
sys.stdin = open("input.txt", "r")


def solve(i, k, cur):
    global res
    global visit
    if cur > res:
        return
    if k == N:
        if cur + adj[i][0] < res:
            res = cur + adj[i][0]
        return

    for j in range(N):
        if not visit[j]:
            visit[j] = True
            solve(j, k + 1, cur + adj[i][j])
            visit[j] = False
    return


T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    visit[0] = True
    res = 100 * N + 1
    solve(0, 1, 0)
    print('#{} {}'.format(test_case, res))