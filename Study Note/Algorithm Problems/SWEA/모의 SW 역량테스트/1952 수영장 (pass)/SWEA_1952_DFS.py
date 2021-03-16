import sys
sys.stdin = open("input.txt", "r")


def solve(cur_cost, d):
    global res
    if cur_cost > Y:
        return
    if d == 12:
        if cur_cost < res:
            res = cur_cost
        return
    elif d > 12:
        return

    solve(cur_cost + plan[d] * D, d + 1)
    solve(cur_cost + M, d + 1)
    solve(cur_cost + M3, d + 3)
    return



T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    D, M, M3, Y = map(int, input().split())
    plan = list(map(int, input().split()))

    res = 2 * Y
    solve(0, 0)
    print('#{} {}'.format(test_case, res if res < Y else Y))