import sys
sys.stdin = open("input.txt", "r")

# 최소 비용 = BFS


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
    visit = [[MAX] * N for _ in range(N)]
    visit[0][0] = 0

    queue = [(0, 0)]
    while len(queue):
        q = queue.pop(0)
        for d in delta:
            nr = q[0] + d[0]
            nc = q[1] + d[1]
            if is_in(nr, nc):
                temp = board[nr][nc] - board[q[0]][q[1]]
                temp = visit[q[0]][q[1]] + 1 + (temp if temp > 0 else 0)

                if visit[nr][nc] > temp:
                    visit[nr][nc] = temp
                    queue.append((nr, nc))

    print('#{} {}'.format(test_case, visit[N - 1][N - 1]))