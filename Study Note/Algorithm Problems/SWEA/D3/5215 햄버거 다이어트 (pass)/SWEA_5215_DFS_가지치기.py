import sys
sys.stdin = open("input.txt", "r")


def solve(current, k, s):
    if current == N:
        return s

    res1 = solve(current + 1, k, s)
    if k + kcal[current] <= L:
        res2 = solve(current + 1, k + kcal[current], s + score[current])
    else:
        return res1

    if res1 >= res2:
        return res1
    else:
        return res2


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, L = map(int, input().split())
    score = []
    kcal = []
    for i in range(N):
        s, k = map(int, input().split())
        score.append(s)
        kcal.append(k)

    s_max = solve(0, 0, 0)
    print('#{} {}'.format(test_case, s_max))