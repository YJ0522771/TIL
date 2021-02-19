import sys
import math
sys.stdin = open("input.txt", "r")

T = int(input())
results = []
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////
    A, B, C, D = map(int, input().split())
    r1 = A / B
    r2 = C / D
    if math.isclose(r1, r2):
        results.append('DRAW')
    elif r1 > r2:
        results.append('ALICE')
    else:
        results.append('BOB')

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, results.pop(0)))