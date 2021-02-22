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
    max_len = 0
    for i in range(1 << N):
        temp = []
        for j in range(N):
            if i & (1 << j):
                temp.append(nums[j])
        state = True
        l = len(temp)
        for j in range(1, l):
            if temp[j - 1] > temp[j]:
                state = False
                break
        if state and max_len < l:
            max_len = l
    res.append(max_len)

for test_case in range(1, T + 1):
    print('#{} {}'.format(test_case, res[test_case - 1]))
