import sys
sys.stdin = open("input.txt", "r")


def solve(k, count, charging):
    global res
    if k == N - 1:
        if res > count:
            res = count
        return

    # 가지치기 검사를 재귀 들어가기 전에 하자 (속도 향상을 위해)
    if count < res:
        solve(k + 1, count + 1, charge[k] - 1)
        if charging > 0:
            solve(k + 1, count, charging - 1)
    return


T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////
    charge = list(map(int, input().split()))
    N = charge.pop(0)
    res = N
    solve(1, 0, charge[0] - 1)
    print('#{} {}'.format(test_case, res))