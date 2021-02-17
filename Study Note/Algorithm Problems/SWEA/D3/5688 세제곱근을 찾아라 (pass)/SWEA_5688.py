import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    result = -1
    for i in range(int(N ** 0.333), int(N ** 0.334) + 1):
        if i ** 3 == N:
            result = i
    print('#{} {}'.format(test_case, result))