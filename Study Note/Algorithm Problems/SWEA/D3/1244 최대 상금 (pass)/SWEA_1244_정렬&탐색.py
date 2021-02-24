import sys
import datetime
current_time = datetime.datetime.now()
sys.stdin = open("input.txt", "r")

def solve(arr, N, K, max_arr, p):
    if K == 0:
        if p == int(''.join(map(str, arr))):
            return True
        else:
            return False
    for i in range(N - 1):
        for j in range(i + 1, N):
            res = list(arr)
            res[i], res[j] = res[j], res[i]
            if solve(res, N, K - 1, max_arr, p):
                return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    nums, K = input().split()
    K = int(K)
    nums = list(map(int, list(nums)))
    perfect = sorted(nums, reverse=True)
    perfect = int(''.join(map(str, perfect)))
    N = len(nums)
    nums2 = list(nums)
    K2 = K

    for i in range(N - 1):
        local_max = nums[i]
        max_i = i
        for j in range(i + 1, N):
            if nums[j] >= local_max:
                local_max = nums[j]
                max_i = j
        if i != max_i:
            nums[i], nums[max_i] = nums[max_i], nums[i]
            K -= 1
        if K == 0:
            break
    res1 = False
    if K > 0:
        renums = False
        for i in range(10):
            if nums.count(i) > 1:
                renums = True
                break
        if not renums:
            if K % 2:
                nums[N - 1], nums[N - 2] = nums[N - 2], nums[N - 1]
    else:
        res1 = solve(nums2, N, K2, 0, perfect)

    res2 = ''.join(map(str, nums))
    if res1:
        print('#{} {}'.format(test_case, perfect))
    else:
        print('#{} {}'.format(test_case, res2))
    
    
    