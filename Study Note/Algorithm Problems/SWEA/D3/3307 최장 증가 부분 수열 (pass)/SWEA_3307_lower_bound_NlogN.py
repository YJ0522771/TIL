import sys
sys.stdin = open("input.txt", "r")

def i_search(L, n):
    f = 0
    t = len(L) - 1
    m = (f + t + 1) // 2
    while f < t:
        if L[m] > n:
            t = m - 1
        else:
            f = m + 1
        m = (f + t + 1) // 2
    return t + 1 if L[t] < n else t 

res = []
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    nums = list(map(int, input().split()))
    L = [nums[0]]           # 길이 i의 오름차순 부분수열 마지막 숫자 중, 가장 작은 숫자 
    for i in range(1, N):
        if nums[i] > L[-1]:
            L.append(nums[i])
        else:
            j = i_search(L, nums[i])
            L[j] = nums[i]
        # print(L)
    res.append(len(L))

for test_case in range(1, T + 1):
    print('#{} {}'.format(test_case, res[test_case - 1]))