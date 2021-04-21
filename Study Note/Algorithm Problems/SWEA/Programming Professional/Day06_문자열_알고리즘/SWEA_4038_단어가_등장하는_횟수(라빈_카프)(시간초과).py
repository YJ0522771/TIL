import sys
sys.stdin = open("input.txt", "r")


def power(a, b):
    t = a
    res = 1
    while b > 0:
        if b % 2:
            res *= t
            b -= 1
            res %= P
        t *= t
        t %= P
        b //= 2
    return res


P = 1000000000000000007     # 2^64
x = 257 # 혹은 259 (소수)
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////
    B = input()
    S = input()

    M = len(S)
    hs = 0
    for i in range(M):
        hs += (ord(S[i]) * power(x, M - 1 - i))
        hs %= P

    hb = 0
    for i in range(M):
        hb += (ord(B[i]) * power(x, M - 1 - i))
        hb %= P

    # print(hs)
    # print(hb)
    res = 0
    if hb == hs:
        res += 1
    for i in range(1, len(B) - M + 1):
        # print('i : ', i)
        hb = (hb * x) % P
        hb -= ((ord(B[i - 1]) * power(x, M)) % P)
        hb += ord(B[i + M - 1])
        hb %= P
        if hb == hs:
            res += 1

    print('#{} {}'.format(test_case, res))
