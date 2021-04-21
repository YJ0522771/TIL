import sys
sys.stdin = open("input.txt", "r")


def max_power(k, SA, SB):
    global tempA
    global tempB
    if k == A:
        if SA + SB > tempA + tempB:
            tempA = SA
            tempB = SB
        return

    if visit[k] == 1:
        max_power(k + 1, BCs[k][3], SB)
    elif visit[k] == 2:
        max_power(k + 1, SA, BCs[k][3])
    elif visit[k] == 3:
        max_power(k + 1, BCs[k][3], SB)
        max_power(k + 1, SA, BCs[k][3])
        max_power(k + 1, BCs[k][3] //2, BCs[k][3] //2)
    max_power(k + 1, SA, SB)


N = 10
delta = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////
    M, A = map(int, input().split())
    pathA = list(map(int, input().split()))
    pathB = list(map(int, input().split()))
    BCs = []
    for _ in range(A):
        BCs.append(tuple(map(int, input().split())))

    curA = [1, 1]
    curB = [10, 10]
    time = 0
    resA = 0
    resB = 0
    while time <= M:
        visit = [0] * A
        for i in range(A):
            disA = abs(curA[0] - BCs[i][0]) + abs(curA[1] - BCs[i][1])
            disB = abs(curB[0] - BCs[i][0]) + abs(curB[1] - BCs[i][1])
            if disA <= BCs[i][2]:
                visit[i] += 1
            if disB <= BCs[i][2]:
                visit[i] += 2

        tempA = 0
        tempB = 0
        max_power(0, 0, 0)

        resA += tempA
        resB += tempB

        if time == M:
            break

        curA[0] += delta[pathA[time]][0]
        curA[1] += delta[pathA[time]][1]
        curB[0] += delta[pathB[time]][0]
        curB[1] += delta[pathB[time]][1]
        time += 1

    print('#{} {}'.format(test_case, resA + resB))







