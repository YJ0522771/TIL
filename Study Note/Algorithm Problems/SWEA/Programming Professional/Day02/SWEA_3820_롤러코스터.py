import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////////////////
    N = int(input())
    ab = []
    for _ in range(N):
        temp = tuple(map(int, input().split()))
        ab.append(temp)
    ab.sort(key=lambda x : (-(x[0] - 1) / x[1]))
    # print(ab)
    res = 1
    for x in ab:
        res *= x[0]
        res += x[1]
        res %= 1000000007
    print('#{} {}'.format(test_case, res))