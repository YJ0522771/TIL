import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    N = int(input())
    nums = list(map(int, input().split()))
    res = 0
    for i in range(1, N - 1):
        if nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
            res += 1
        elif nums[i] < nums[i - 1] and nums[i] > nums[i + 1]:
            res += 1
    print('#{} {}'.format(test_case, res))