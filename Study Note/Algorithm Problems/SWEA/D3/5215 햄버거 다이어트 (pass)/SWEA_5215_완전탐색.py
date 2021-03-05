import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, L = map(int, input().split())
    score = []
    kcal = []
    for i in range(N):
        s, k = map(int, input().split())
        score.append(s)
        kcal.append(k)
    
    result = []
    for i in range(1, 1 << N):
        s = 0
        k = 0
        for j in range(N):
            if i & (1 << j):
                s += score[j]
                k += kcal[j]
    print('#{} {}'.format(test_case, max(result)))
