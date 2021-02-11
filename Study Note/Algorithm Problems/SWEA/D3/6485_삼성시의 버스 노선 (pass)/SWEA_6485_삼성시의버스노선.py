import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    print('#{}'.format(test_case), end='')

    N = int(input())    # 버스 노선 수

    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A += [a]
        B += [b]

    P = int(input())    # 버스 정류장 수

    station = []
    for i in range(P):
        station += [int(input())]

    count = [0] * P
    for i in range(N):
        for j in range(P):
            if station[j] >= A[i] and station[j] <= B[i]:
                count[j] += 1

    for i in range(P):
        print(' {}'.format(count[i]), end='')
    print()
