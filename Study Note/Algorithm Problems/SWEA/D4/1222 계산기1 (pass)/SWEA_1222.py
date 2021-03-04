import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////
    N = int(input())
    string = input()
    res = 0
    for s in string:
        if not s == '+':
            res += int(s)
    print('#{} {}'.format(test_case, res))