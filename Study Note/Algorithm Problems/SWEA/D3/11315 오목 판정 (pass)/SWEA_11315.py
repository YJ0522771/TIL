import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#{}'.format(test_case), end=' ')
    N = int(input())

    board = []
    for i in range(N):
        board += [input()]
    
    result = False
    # 가로 검색
    for i in range(N):
        if result:
            break
        for j in range(N - 4):
            if result:
                break
            for k in range(5):
                if board[i][j + k] == '.':
                    break
                elif k == 4:
                    result = True
    
    if result:
        print('YES')
        continue

    # 세로 검색
    for i in range(N - 4):
        if result:
            break
        for j in range(N):
            if result:
                break
            for k in range(5):
                if board[i + k][j] == '.':
                    break
                elif k == 4:
                    result = True
    
    if result == True:
        print('YES')
        continue

    # \ 검색
    for i in range(N - 4):
        if result == True:
            break
        for j in range(N - 4):
            if result == True:
                break
            for k in range(5):
                if board[i + k][j + k] == '.':
                    break
                elif k == 4:
                    result = True
    
    if result == True:
        print('YES')
        continue

    # / 검색
    for i in range(4, N):
        if result == True:
            break
        for j in range(N - 4):
            if result == True:
                break
            for k in range(5):
                if board[i - k][j + k] == '.':
                    break
                elif k == 4:
                    result = True

    if result == True:
        print('YES')
        continue

    print('NO')