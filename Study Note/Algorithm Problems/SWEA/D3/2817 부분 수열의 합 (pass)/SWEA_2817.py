import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K =  map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i & (1 << j):
                s += nums[j]
        if s == K:
            count += 1

    print('#{} {}'.format(test_case, count))