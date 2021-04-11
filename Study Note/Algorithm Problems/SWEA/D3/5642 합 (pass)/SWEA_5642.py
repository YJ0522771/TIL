import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////
    N = int(input())
    nums = list(map(int, input().split()))
    temp = 0
    res = -1001
    for i in range(N):
        temp += nums[i]
        if res < temp:
            res = temp
        if temp < 0:
            temp = 0

    print('#{} {}'.format(test_case, res))
