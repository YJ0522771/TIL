import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////
    N = int(input())
    N = 100
    board = [input() for _ in range(N)]
    max_len = 0
    for M in range(1, 101):
        # 가로 검사
        for i in range(N):
            for j in range(N - M + 1):
                state = True
                for k in range(M // 2):
                    if board[i][j + k] != board[i][j + M - 1 - k]:
                        state = False
                        break
                if state:
                    break
            if state:
                break

        if state:
            max_len = M
            continue

        # 세로 검사
        for i in range(N):
            for j in range(N - M + 1):
                state = True
                for k in range(M // 2):
                    if board[j + k][i] != board[j + M - 1 - k][i]:
                        state = False
                        break
                if state:
                    break
            if state:
                break
        if state:
            max_len = M

    print('#{} {}'.format(test_case, max_len))