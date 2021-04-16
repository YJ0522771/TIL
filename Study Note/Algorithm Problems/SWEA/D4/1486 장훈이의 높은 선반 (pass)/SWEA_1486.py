import sys
sys.stdin = open("input.txt", "r")


def solve(k, h):
    global res
    if k >= N:
        if h >= B and h - B < res:
            res = h - B
        return
    if h >= B + res:
        return

    solve(k + 1, h + H[k])
    solve(k + 1, h)
    return


T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////
    N, B = map(int, input().split())
    if N == 1:
        print('#{} {}'.format(test_case, int(input()) - B))
        continue

    H = list(map(int, input().split()))
    res = sum(H)
    solve(0, 0)
    print('#{} {}'.format(test_case, res))