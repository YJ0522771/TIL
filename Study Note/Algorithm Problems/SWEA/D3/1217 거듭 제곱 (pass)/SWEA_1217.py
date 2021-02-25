import sys
sys.stdin = open("input.txt", "r")

def pow(n, m):
    if m == 1:
        return n
    return n * pow(n, m - 1)

T = 10
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    tc = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, pow(N, M)))
