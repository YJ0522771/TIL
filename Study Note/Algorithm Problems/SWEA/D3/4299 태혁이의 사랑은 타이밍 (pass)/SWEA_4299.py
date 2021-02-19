import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////
    D, H, M = map(int, input().split())

    H_minus = False
    if M >= 11:
        M -= 11
    else:
        M = 60 - (11 - M)
        H_minus = True

    D_minus = False
    if H >= (11 + H_minus):
        H -= (11 + H_minus)
    else:
        H = 24 - (11 - H + H_minus)
        D_minus = True

    if D >= (11 + D_minus):
        D -= (11 + D_minus)
    else:
        print('#{} -1'.format(test_case))
        continue

    print('#{} {}'.format(test_case, M + (60 * (H + D * 24))))