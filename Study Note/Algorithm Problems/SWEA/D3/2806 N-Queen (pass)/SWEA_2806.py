import sys
sys.stdin = open("input.txt", "r")


def solve(cur):
    global visit
    global res
    if cur == N:
        res += 1
        return
    for i in range(N):
        if is_possible(cur, i):
            visit[cur][i] = 1
            solve(cur + 1)
            visit[cur][i] = 0
    return


def is_possible(r, c):
    for d in delta:
        nr = r + d[0]
        nc = c + d[1]
        while is_in(nr, nc):
            if visit[nr][nc]:
                return False
            nr += d[0]
            nc += d[1]
    return True


def is_in(r, c):
    if r >= 0 and r < N and c >= 0 and c < N:
        return True
    return False


delta = [(1, 0), (-1, 0), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    visit = [[0] * N for _ in range(N)]
    res = 0
    solve(0)
    print('#{} {}'.format(test_case, res))