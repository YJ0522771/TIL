import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////
    N = int(input())
    board = [input() for _ in range(8)]
    count = 0
    # 가로 검사
    for i in range(8):
        for j in range(8 - N + 1):
            state = True
            for k in range(N // 2):
                if board[i][j + k] != board[i][j + N - 1 - k]:
                    state = False
                    break
            if state:
                count += 1

    # 세로 검사
    for i in range(8):
        for j in range(8 - N + 1):
            state = True
            for k in range(N // 2):
                if board[j + k][i] != board[j + N - 1 - k][i]:
                    state = False
                    break
            if state:
                count += 1

    print('#{} {}'.format(test_case, count))