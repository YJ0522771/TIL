import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////////
    A, B = input().split()
    A_N = len(A)
    B_N = len(B)
    count = A_N
    i = 0
    while i < A_N - B_N + 1:
        state = True
        for j in range(B_N):
            if A[i + j] != B[j]:
                state = False
                break
        if state:
            count -= (B_N - 1)
            i += B_N
        else:
            i += 1

    print('#{} {}'.format(test_case, count))