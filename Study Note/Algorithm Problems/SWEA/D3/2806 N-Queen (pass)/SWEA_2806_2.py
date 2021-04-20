import sys
sys.stdin = open("input.txt", "r")


def solve(cur):
    global visit
    global res
    if cur == N:
        res += 1
        return
    for i in range(N):
        if not visit[cur][i]:
            Queen(cur, i, 1)
            solve(cur + 1)
            Queen(cur, i, -1)
    return


def Queen(r, c, p):
    global visit
    visit[r][c] += p
    for d in delta:
        nr = r + d[0]
        nc = c + d[1]
        while is_in(nr, nc):
            visit[nr][nc] += p
            nr += d[0]
            nc += d[1]
    return


def is_in(r, c):
    if r >= 0 and r < N and c >= 0 and c < N:
        return True
    return False


delta = [(1, 0), (-1, 0), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    visit = [[0] * N for _ in range(N)]
    res = 0
    solve(0)
    print('#{} {}'.format(test_case, res))