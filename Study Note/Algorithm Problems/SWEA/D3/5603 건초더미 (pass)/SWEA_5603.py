import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////
    N = int(input())
    l = [int(input()) for _ in range(N)]
    avg = sum(l) // N
    res = 0
    for i in l:
        res += abs(i - avg)
    print('#{} {}'.format(test_case, res // 2))

