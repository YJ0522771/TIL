import sys
sys.stdin = open("input.txt", "r")


def solve(k, i, cur):
    global res
    if cur > res:
        return
    if k == N:
        if res > cur + adj[i][N + 1]:
            res = cur + adj[i][N + 1]
        return

    for j in range(1, N + 1):
        if visit[j]:
            continue
        visit[j] = True
        solve(k + 1, j, cur + adj[i][j])
        visit[j] = False
    return


T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////////
    N = int(input())
    ll = list(map(int, input().split()))
    info = [(ll[0], ll[1])]
    for i in range(4, len(ll), 2):
        info.append((ll[i], ll[i + 1]))
    info.append((ll[2], ll[3]))
    # print(info)

    adj = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(N + 2):
        for j in range(N + 2):
            adj[i][j] = abs(info[i][0] - info[j][0]) + abs(info[i][1] - info[j][1])
    # for i in range(N + 2):
    #     print(adj[i])

    visit = [False] * (N + 2)
    res = 1000000
    solve(0, 0, 0)
    print('#{} {}'.format(test_case, res))

