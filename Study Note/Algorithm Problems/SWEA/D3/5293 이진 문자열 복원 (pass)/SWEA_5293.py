import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////
    A, B, C, D = map(int, input().split())
    if A > 0 and D > 0 and B == 0 and C == 0:
        res = 'impossible'
    elif abs(B - C) >= 2:
        res = 'impossible'
    else:
        aa = '0' * A
        dd = '1' * D
        if B > C:
            bc = '01' * B
            res = aa + bc + dd
        elif C > B:
            cb = '10' * C
            res = dd + cb + aa
        else:
            if A < D:
                cc = '10' * C
                res = dd + cc + aa + '1'
            else:
                bb = '01' * B
                res = aa + bb + dd + '0'

    print('#{} {}'.format(test_case, res))