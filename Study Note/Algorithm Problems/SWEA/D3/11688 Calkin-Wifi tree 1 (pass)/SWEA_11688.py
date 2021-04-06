import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    l = list(input())
    a = 1
    b = 1
    print(len(l))
    for c in l:
        if c == 'L':
            b = a + b
        else:
            a = a + b
    print('#{} {} {}'.format(test_case, a, b))
