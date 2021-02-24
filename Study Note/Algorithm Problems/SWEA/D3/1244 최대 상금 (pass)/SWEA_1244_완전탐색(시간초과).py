import sys
import datetime
current_time = datetime.datetime.now()
sys.stdin = open("input.txt", "r")

def solve(arr, N, K, max_arr, p):
    if K == 0:
        return int(''.join(map(str, arr)))
    for i in range(N - 1):
        for j in range(i + 1, N):
            res = list(arr)
            res[i], res[j] = res[j], res[i]
            temp = solve(res, N, K - 1, max_arr, p)
            if temp > max_arr:
                max_arr = temp
                if max_arr == p:
                    break
        if max_arr == p:
            break
        
    return max_arr

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
    nums = solve(nums, N, K, 0, perfect)
    
    print('#{} {} {}'.format(test_case, nums, datetime.datetime.now() - current_time))