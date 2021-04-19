import sys
sys.stdin = open("input.txt", "r")


def merge_sort(arr):
    global res
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # print(left, right)
    if left[len(left) - 1] > right[len(right) - 1]:
        res += 1

    temp = []
    l = 0
    r = 0
    while True:
        if left[l] > right[r]:
            temp.append(right[r])
            r += 1
        else:
            temp.append(left[l])
            l += 1

        if l >= len(left) or r >= len(right):
            break

    if l < len(left):
        temp += left[l:]
    elif r < len(right):
        temp += right[r:]

    # print(temp)
    return temp


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
    nums = merge_sort(nums)

    print('#{} {} {}'.format(test_case, nums[N // 2], res))