import sys
sys.stdin = open("input.txt", "r")

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

    N = len(nums)
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
    
    if K > 0:
        renums = False
        for i in range(10):
            if nums.count(i) > 1:
                renums = True
                break
        if not renums:
            if K % 2:
                nums[N - 1], nums[N - 2] = nums[N - 2], nums[N - 1]
    
    print('#{} {}'.format(test_case, ''.join(map(str, nums))))