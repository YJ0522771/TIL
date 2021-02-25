import sys
sys.stdin = open("input.txt", "r")


def is_in(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    return False


# 위, 아래, 왼, 오, 왼위, 오위, 왼아래, 오아래 (x, y)
delta = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    # 초기 위치
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1

    for _ in range(M):
        x, y, c = map(int, input().split())
        x, y = x - 1, y - 1
        board[y][x] = c
        c2 = 2 if c - 2 else 1

        for case in range(8):
            m = 1
            change = False
            nx = x + (m + 1) * delta[case][0]
            ny = y + (m + 1) * delta[case][1]
            while is_in(nx, ny) and board[y + m * delta[case][1]][x + m * delta[case][0]] == c2:
                m += 1
                if board[y + m * delta[case][1]][x + m * delta[case][0]] == c:
                    change = True
                    break
                nx = x + (m + 1) * delta[case][0]
                ny = y + (m + 1) * delta[case][1]
            if change:
                for i in range(1, m):
                    board[y + i * delta[case][1]][x + i * delta[case][0]] = c

    count = [0] * 3
    for i in range(N):
        for n in board[i]:
            count[n] += 1
    print('#{} {} {}'.format(test_case, count[1], count[2]))