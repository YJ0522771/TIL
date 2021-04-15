import sys
sys.stdin = open("5186_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////
    R = float(input())
    res = ''
    while R > 0.0000001:
        R *= 2
        if R >= 1:
            res += '1'
            R -= 1
        else:
            res += '0'
        if len(res) > 12:
            res = 'overflow'
            break
    print('#{} {}'.format(test_case, res))

