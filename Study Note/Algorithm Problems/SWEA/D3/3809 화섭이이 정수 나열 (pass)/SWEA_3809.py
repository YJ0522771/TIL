import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////
    N = int(input())
    nums = list(input().split())
    while N > len(nums):
        nums += list(input().split())

    # print(nums)
    nums = ''.join(nums)
    for i in range(1000):
        if str(i) not in nums:
            break

    print('#{} {}'.format(test_case, i))
