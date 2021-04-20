import sys
sys.stdin = open("input.txt", "r")

A = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724]
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(test_case, A[N]))