import sys
sys.stdin = open("input.txt", "r")


def solve(r, c, num):
    global num_set
    if len(num) >= 7:
        num_set.add(num)
        return

    for d in delta:
        nr = r + d[0]
        nc = c + d[1]
        if is_in(nr, nc):
            solve(nr, nc, num + str(board[nr][nc]))
    return


def is_in(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
N = 4
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    board = [list(map(int, input().split())) for _ in range(N)]
    num_set = set([])

    for i in range(N):
        for j in range(N):
            solve(i, j, '')

    print('#{} {}'.format(test_case, len(num_set)))
