import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    L, U, X = map(int, input().split())
    if X < L:
        print('#{} {}'.format(test_case, L - X))
    elif X > U:
        print('#{} -1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))