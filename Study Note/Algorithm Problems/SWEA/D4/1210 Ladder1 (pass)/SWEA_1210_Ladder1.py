import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////
    N = int(input())

    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    for i in range(100):
        row = 0
        col = i
        if ladder[row][col] == 0:
            continue
        direct = 0
        while row < 99:
            if not direct:
                if col > 0 and ladder[row][col - 1] == 1:
                    direct = -1
                    col -= 1
                elif col < 99 and ladder[row][col + 1] == 1:
                    direct = 1
                    col += 1
                else:
                    row += 1
            elif direct == 1:
                if col < 99 and ladder[row][col + 1] == 1:
                    col += 1
                else:
                    direct = 0
                    row += 1
            else:
                if col > 0 and ladder[row][col - 1] == 1:
                    col -= 1
                else:
                    direct = 0
                    row += 1
        if ladder[row][col] == 2:
            break
    print('#{} {}'.format(N, i))