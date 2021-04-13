import sys
sys.stdin = open("input.txt", "r")

# parametric search
# 특정 x에 대해 인접한 수와의 차이가 x이하가 되도록 만들 수 있는가
def promising(x):
    t1 = [0] * N
    t1[0] = nums[0]
    for i in range(1, N):
        t1[i] = min(t1[i - 1] + x, nums[i])

    t2 = [0] * N
    t2[N - 1] = min(nums[N - 1], t1[N - 1])
    for i in range(N - 2, -1, -1):
        t2[i] = min(t2[i + 1] + x, nums[i], t1[i])
    # print(x, t2)
    s = 0
    for i in range(N):
        d = nums[i] - t2[i]
        if d > 0:
            s += d
        if s > K:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    # binary search
    left = 0
    right = 100000
    while left <= right:
        mid = (left + right) // 2
        tf = promising(mid)
        if tf:
            right = mid - 1
        else:
            left = mid + 1
    if tf:
        print('#{} {}'.format(test_case, mid))
    else:
        print('#{} {}'.format(test_case, mid + 1))

