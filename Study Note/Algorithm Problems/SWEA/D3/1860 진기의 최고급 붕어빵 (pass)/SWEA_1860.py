import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////
    N, M, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    state = True
    for i in range(len(p)):
        if (p[i] // M) * K - i <= 0:
            state = False
            break
    if state:
        print('#{} Possible'.format(test_case))
    else:
        print('#{} Impossible'.format(test_case))