import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    nums = [] * 100
    for i in range(100):
        nums.append(list(map(int, input().split())))

    result = 0

    # 가로
    for i in range(100):
        s = 0
        for j in range(100):
            s += nums[i][j]
        if s > result:
            result = s
    # 세로
    for i in range(100):
        s = 0
        for j in range(100):
            s += nums[j][i]
        if s > result:
            result = s
    # \
    s = 0
    for i in range(100):
        s += nums[i][i]
    if s > result:
        result = s
    # /
    s = 0
    for i in range(100):
        s += nums[i][99 - i]
    if s > result:
        result = s

    print('#{} {}'.format(N, result))
