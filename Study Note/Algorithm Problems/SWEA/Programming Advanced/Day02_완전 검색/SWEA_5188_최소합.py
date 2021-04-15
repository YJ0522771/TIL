import sys
sys.stdin = open("input.txt", "r")


def solve(r, c, cur):
    global res
    if cur > res:
        return
    if r == N - 1 and c == N - 1:
        if cur < res:
            res = cur
        return

    for d in delta:
        nr = r + d[0]
        nc = c + d[1]
        if is_in(nr, nc):
            solve(nr, nc, cur + nums[nr][nc])
    return


def is_in(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


delta = [(0, 1), (1, 0)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    res = 2000
    solve(0, 0, nums[0][0])
    print('#{} {}'.format(test_case, res))