import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    V = []
    C = []
    for _ in range(N):
        v, c = map(int, input().split())
        V.append(v)
        C.append(c)

    res = 0
    for i in range(1 << N):
        v_sum = 0
        c_sum = 0
        state = True
        for j in range(N):
            if i & (1 << j):
                v_sum += V[j]
                c_sum += C[j]
                if v_sum > K:
                    state = False
                    break
        if state and c_sum > res:
            res = c_sum

    print('#{} {}'.format(test_case, res))



