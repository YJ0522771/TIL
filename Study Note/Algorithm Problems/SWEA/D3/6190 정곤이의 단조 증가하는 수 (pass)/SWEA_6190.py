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
    nums = list(map(int, input().split()))
    result = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            temp = nums[i] * nums[j]
            last = temp % 10
            temp //= 10
            while temp > 0:
                if last < temp % 10:
                    break
                last = temp % 10
                temp //= 10
            if temp > 0:
                continue
            else:
                if result < nums[i] * nums[j]:
                    result = nums[i] * nums[j]
    if N == 1:
        result = nums[0] 
    print('#{} {}'.format(test_case, result if result else -1))