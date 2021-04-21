import sys
sys.stdin = open("input.txt", "r")


def solve(r, c, count, d):
    global res
    global visit
    if r == i and c == j and d == 3:
        if res < count:
            res = count
        return

    nr = r + delta[d][0]
    nc = c + delta[d][1]
    if is_in(nr, nc) and not visit[cafes[nr][nc]]:
        visit[cafes[nr][nc]] = True
        solve(nr, nc, count + 1, d)
        visit[cafes[nr][nc]] = False

    # 방향이 3 미만일 때만 방향 전환이 가능하다.
    if d < 3:
        d += 1
        nr = r + delta[d][0]
        nc = c + delta[d][1]
        if is_in(nr, nc) and not visit[cafes[nr][nc]]:
            visit[cafes[nr][nc]] = True
            solve(nr, nc, count + 1, d)
            visit[cafes[nr][nc]] = False
    return


def is_in(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


# 시계방향만 탐색
# 한 방향으로의 순회만 탐색하면 된다. (순회 방향을 바꾸어 탐색하면 시작점을 바꾸었을 때 중복이 발생)
delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    # 해당 디저트를 먹었는 지 확인
    visit = [False] * 101
    for i in range(N):
        for j in range(N):
            # 마지막에 시작점으로 돌아올 수 있게 시작할 때는 시작점에 방문 표시를 하지 않는다.
            solve(i, j, 0, 0)

    print('#{} {}'.format(test_case, res if res else -1))