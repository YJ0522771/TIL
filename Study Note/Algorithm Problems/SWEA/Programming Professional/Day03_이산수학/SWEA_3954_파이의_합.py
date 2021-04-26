import sys
sys.stdin = open("input.txt", "r")


phi = [i for i in range(1000001)]
phi[1] = 1
visit = [False] * 1000001
for i in range(2, 1000001):
    if not visit[i]:
        for j in range(i, 1000001, i):
            visit[j] = True
            phi[j] *= (i - 1)
            phi[j] //= i

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////
    a, b = map(int, input().split())

    res = 0
    for i in range(a, b + 1):
        res += phi[i]

    print('#{} {}'.format(test_case, res))