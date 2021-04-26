import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    S = input()
    N = len(S)

    res = 1
    for i in range(1, N):
        if N % i:
            continue

        state = True
        temp = S[:i]
        for j in range(N):
            if S[j] != temp[j % i]:
                state = False
                break
        if state:
            res = N // i
            break

    print('#{} {}'.format(test_case, res))
