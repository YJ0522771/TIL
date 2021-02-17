import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N = 7
    nums = list(map(int, input().split()))
    sums = []
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N): 
                temp = nums[i] + nums[j] + nums[k]
                if not temp in sums:
                    sums.append(temp)
    sums.sort(reverse=True)
    print('#{} {}'.format(test_case, sums[4]))