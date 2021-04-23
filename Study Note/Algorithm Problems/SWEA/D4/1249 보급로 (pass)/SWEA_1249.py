import sys
sys.stdin = open("input.txt", "r")


def is_in(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


MAX = 1000000
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////
    N = int(input())
    mm = [list(map(int, list(input()))) for _ in range(N)]
    # print(mm)
    visit = [[MAX] * N for _ in range(N)]
    visit[0][0] = 0

    queue = [(0, 0)]
    while len(queue):
        q = queue.pop(0)
        cur = visit[q[0]][q[1]]

        for d in delta:
            nr = q[0] + d[0]
            nc = q[1] + d[1]
            if is_in(nr, nc) and visit[nr][nc] > cur + mm[nr][nc]:
                visit[nr][nc] = cur + mm[nr][nc]
                queue.append((nr, nc))
                # print(nr, nc, visit[nr][nc])

    print('#{} {}'.format(test_case, visit[N - 1][N - 1]))
