import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////
    N, A, B = map(int, input().split())
    minimum = (A + B) * N * N
    for i in range(1, N + 1):
        for j in range(i, N // i + 1):
            C = i
            R = j
            temp = (A * (R - C)) + (B * (N - (R * C)))
            if temp < minimum:
                minimum = temp
    print('#{} {}'.format(test_case, minimum))
