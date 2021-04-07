import sys
sys.stdin = open("input.txt", "r")

M = 1234567891

fac = [1]
for i in range(1, 1000001):
    fac.append((fac[i-1] * i) % M)

res = []
T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////
    N, R = map(int, input().split())

    # R!(N-R)!의 M-2 제곱
    t = fac[R] * fac[N - R]
    temp = 1
    l = M - 2
    while l > 0:
        if (l % 2) == 1:
            temp *= t
            l -= 1
            temp %= M
        t *= t
        t %= M
        l /= 2

    # for _ in range(1234567891 - 2):
    #     temp *= t
    #     temp %= 1234567891
    temp *= fac[N]
    temp %= M
    res.append('#{} {}'.format(test_case, temp))

for t in range(T):
    print(res[t])