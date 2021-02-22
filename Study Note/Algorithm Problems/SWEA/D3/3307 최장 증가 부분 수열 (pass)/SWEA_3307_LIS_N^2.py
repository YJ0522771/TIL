import sys
sys.stdin = open("input.txt", "r")

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
    LIS = [1]       # nums[i]를 끝으로 하는 오름차순 부분수열 중 가장 긴 것의 길이 
    for i in range(1, N):
        max_LIS = 0
        for j in range(i):
            if nums[i] >= nums[j] and max_LIS < LIS[j]:
                max_LIS = LIS[j]
        LIS.append(max_LIS + 1)

    res.append(max(LIS))

for test_case in range(1, T + 1):
    print('#{} {}'.format(test_case, res[test_case - 1]))