import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    D, M, M3, Y = map(int, input().split())
    plan = list(map(int, input().split()))

    min_cost = [0] * 13

    for i in range(1, 13):
        min_cost[i] = min_cost[i - 1] + min(plan[i - 1] * D, M)
        if i > 2:
            min_cost[i] = min(min_cost[i], min_cost[i - 3] + M3)

    if min_cost[12] < Y:
        print('#{} {}'.format(test_case, min_cost[12]))
    else:
        print('#{} {}'.format(test_case, Y))