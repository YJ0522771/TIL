import sys
sys.stdin = open("input.txt", "r")


def solve(k, cur):
    global opers
    global min_res
    global max_res
    if k == N - 1:
        if cur < min_res:
            min_res = cur
        if cur > max_res:
            max_res = cur
        return

    for i in range(4):
        if opers[i]:
            opers[i] -= 1
            if i == 0:
                solve(k + 1, cur + nums[k + 1])
            elif i == 1:
                solve(k + 1, cur - nums[k + 1])
            elif i == 2:
                solve(k + 1, cur * nums[k + 1])
            else:
                solve(k + 1, int(cur / nums[k + 1]))
            opers[i] += 1
    return


T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    N = int(input())
    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    min_res = 1000000000
    max_res = -1000000000
    solve(0, nums[0])
    print('#{} {}'.format(test_case, max_res - min_res))