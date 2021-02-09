import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    print('#{}'.format(test_case), end='')

    N, Q = map(int, input().split())
    box = [0] * N

    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = i + 1

    for b in box:
        print(' {}'.format(b), end='')
    print()



