import sys
sys.stdin = open("input.txt", "r")

# Dijkstra
# 하고 보니 별로 다를 건 없어 보이네
# 최소 간선 찾는 거 때문에 시간 초과


def is_in(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    MAX = 1000 * N * N

    visit = [[False] * N for _ in range(N)]
    visit[0][0] = True

    D = [[MAX] * N for _ in range(N)]
    temp = board[0][1] - board[0][0]
    D[0][1] = (temp if temp > 0 else 0) + 1
    temp = board[1][0] - board[0][0]
    D[1][0] = (temp if temp > 0 else 0) + 1

    count = 0
    while count < N * N:
        mm = MAX
        e = (0, 0)
        for i in range(N):
            for j in range(N):
                if not visit[i][j] and D[i][j] < mm:
                    mm = D[i][j]
                    e = (i, j)

        visit[e[0]][e[1]] = True
        count += 1
        for d in delta:
            nr = e[0] + d[0]
            nc = e[1] + d[1]
            if is_in(nr, nc) and not visit[nr][nc]:
                temp = board[nr][nc] - board[e[0]][e[1]]
                temp = mm + 1 + (temp if temp > 0 else 0)
                if D[nr][nc] > temp:
                    D[nr][nc] = temp

    print('#{} {}'.format(test_case, D[N - 1][N - 1]))

