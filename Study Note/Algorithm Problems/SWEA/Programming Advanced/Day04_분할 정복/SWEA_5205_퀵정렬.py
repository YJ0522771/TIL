import sys
sys.stdin = open("input.txt", "r")


def quick_sort(left, right):
    global nums
    if left >= right:
        return

    # print(left, right)
    # print(arr)
    p = nums[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= right and nums[i] <= p:
            i += 1
        while j > left and nums[j] >= p:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[j] = nums[j], nums[left]

    quick_sort(left, j - 1)
    quick_sort(j + 1, right)

    return


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    N = int(input())
    nums = list(map(int, input().split()))

    quick_sort(0, N - 1)
    print(nums)
    print('#{} {}'.format(test_case, nums[N // 2]))
