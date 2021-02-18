import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = board[N // 2][N // 2] = 2
    board[N // 2 - 1][N // 2] = board[N // 2][N // 2 - 1] = 1

    for _ in range(M):
        x, y, c = map(int, input().split())
        x, y = x - 1, y - 1
        board[y][x] = c
        c2 = 2 if c - 2 else 1

        # 위
        m = 1
        change = False
        while y - m > 0 and board[y - m][x] == c2:
            m += 1
            if board[y - m][x] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y - i][x] = c

        # 아래
        m = 1
        change = False
        while y + m < N - 1 and board[y + m][x] == c2:
            m += 1
            if board[y + m][x] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y + i][x] = c

        # 왼쪽
        m = 1
        change = False
        while x - m > 0 and board[y][x - m] == c2:
            m += 1
            if board[y][x - m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y][x - i] = c

        # 오른쪽
        m = 1
        change = False
        while x + m < N - 1 and board[y][x + m] == c2:
            m += 1
            if board[y][x + m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y][x + i] = c

        # 왼위
        m = 1
        change = False
        while x - m > 0 and y - m > 0 and board[y - m][x - m] == c2:
            m += 1
            if board[y - m][x - m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y - i][x - i] = c
        
        # 오위
        m = 1
        change = False
        while x + m < N - 1 and y - m > 0 and board[y - m][x + m] == c2:
            m += 1
            if board[y - m][x + m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y - i][x + i] = c

        # 왼아래
        m = 1
        change = False
        while x - m > 0 and y + m < N - 1 and board[y + m][x - m] == c2:
            m += 1
            if board[y + m][x - m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y + i][x - i] = c

        # 오아래
        m = 1
        change = False
        while x + m < N - 1 and y + m < N - 1 and board[y + m][x + m] == c2:
            m += 1
            if board[y + m][x + m] == c:
                change = True
                break
        if change:
            for i in range(1, m):
                board[y + i][x + i] = c

    count = [0] * 3
    for i in range(N):
        for n in board[i]:
            count[n] += 1
    print('#{} {} {}'.format(test_case, count[1], count[2]))

