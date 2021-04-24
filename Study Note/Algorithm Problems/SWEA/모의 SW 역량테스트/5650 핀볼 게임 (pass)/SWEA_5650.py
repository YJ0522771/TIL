import sys
sys.stdin = open("input.txt", "r")


def simulation(sr, sc, sd):
    score = 0
    r = sr
    c = sc
    d = sd
    # print(r, c, d)
    while True:
        # print(sr, sc, r, c, d)
        nr = r + delta[d][0]
        nc = c + delta[d][1]

        # 종료 조건
        if (nr == sr and nc == sc) or info[nr][nc] == -1:
            return score

        # 벽이나 5번 블록에 부딪혔을 때
        elif info[nr][nc] == 5:
            d = d_change[0][d]
            score += 1

        # 웜홀을 만났을 때
        elif info[nr][nc] > 5:
            temp = wormholes[info[nr][nc]]
            # 반대편 웜홀로 이동
            if (nr, nc) == temp[0]:
                r = temp[1][0]
                c = temp[1][1]
                continue
            else:
                r = temp[0][0]
                c = temp[0][1]
                continue

        # 1~4번 블록을 만났을 때 방향 전환
        elif info[nr][nc] > 0:
            d = d_change[info[nr][nc]][d]
            score += 1

        r = nr
        c = nc


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d_change = [[1, 0, 3, 2], # 벽, 5번
            [1, 3, 0, 2], # 1번
            [3, 0, 1, 2], # 2번
            [2, 0, 3, 1], # 3번
            [1, 2, 3, 0]] # 4번
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////
    N = int(input())
    info = [[5] + list(map(int, input().split())) + [5] for _ in range(N)]
    info = [[5] * (N + 2)] + info + [[5] * (N + 2)]

    wormholes = {6: [], 7: [], 8: [], 9: [], 10: []}
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if info[i][j] > 5:
                wormholes[info[i][j]].append((i, j))

    res = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if info[i][j] == 0:
                for d in range(4):
                    temp = simulation(i, j, d)
                    if res < temp:
                        res = temp

    print('#{} {}'.format(test_case, res))
