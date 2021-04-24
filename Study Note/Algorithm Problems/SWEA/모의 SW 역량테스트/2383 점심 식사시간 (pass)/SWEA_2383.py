import sys
sys.stdin = open("input.txt", "r")


def simulation(d_info, s_info):
    # print(d_info)
    # print(s_info)
    p_count = 0
    p_state = [True] * M
    s_queue = [[], []]
    time = 0
    while p_count < M:
        for i in range(M):
            if d_info[i] >= 0:
                d_info[i] -= 1
            elif p_state[i] and d_info[i] != 0:
                ss = s_info[i]
                s_queue[ss].append(S[ss][2])
                p_state[i] = False

        for i in range(2):
            for j in range(min(3, len(s_queue[i]))):
                s_queue[i][j] -= 1
            while len(s_queue[i]) and s_queue[i][0] == 0:
                s_queue[i].pop(0)
                p_count += 1

        # print(s_queue)
        # print(p_state)

        time += 1
    # print(time)
    return time


def dfs(k, d_info, s_info):
    global res
    if k == M:
        d_temp = list(d_info)
        s_temp = list(s_info)
        temp = simulation(d_temp, s_temp)
        if res > temp:
            res = temp
        return

    d_info.append(P[k][0])
    s_info.append(0)
    dfs(k + 1, d_info, s_info)
    d_info.pop()
    s_info.pop()
    d_info.append(P[k][1])
    s_info.append(1)
    dfs(k + 1, d_info, s_info)
    d_info.pop()
    s_info.pop()
    return



T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    S = []
    for i in range(N):
        for j in range(N):
            if info[i][j] > 1:
                S.append((i, j, info[i][j]))

    P = []
    for i in range(N):
        for j in range(N):
            if info[i][j] == 1:
                d1 = abs(S[0][0] - i) + abs(S[0][1] - j)
                d2 = abs(S[1][0] - i) + abs(S[1][1] - j)
                P.append([d1, d2])
    M = len(P)
    # print(P)

    res = 1000000
    dfs(0, [], [])
    print('#{} {}'.format(test_case, res))