import sys
sys.stdin = open("input.txt", "r")


def is_possible(road):
    # 다음 칸으로 움직일 수 있는 지
    move = [False] * N
    # 경사로를 놓을 수 있는 지
    slope = [True] * N

    for j in range(N - 1):
        if move[j]:
            continue

        if road[j] == road[j + 1]:
            move[j] = True
        elif road[j] - 1 == road[j + 1]:
            count = 0
            for k in range(j + 1, N):
                if road[j + 1] == road[k] and slope[k]:
                    count += 1
                else:
                    break
            if count >= X:
                # 다음 칸으로 갈 수 있는 지 여부이므로, 마지막 칸은 채우지 않는다.
                for k in range(j + 1, j + X):
                    move[k] = True
                    # 한 번 놓은 곳에는 다른 경사로를 놓을 수 없음
                    slope[k] = False
                slope[j + X] = False
                move[j] = True
            else:
                return False
        elif road[j] + 1 == road[j + 1]:
            count = 0
            for k in range(j, -1, -1):
                if road[j] == road[k] and slope[k]:
                    count += 1
                else:
                    break
            if count >= X:
                for k in range(j, j - X, -1):
                    move[k] = True
                    slope[k] = False
                move[j] = True
            else:
                return False

    # print(move)
    for k in range(N - 1):
        if not move[k]:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////
    N, X = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        road = [0] * N
        # 가로
        for j in range(N):
            road[j] = info[i][j]

        if is_possible(road):
            res += 1

        # 세로
        for j in range(N):
            road[j] = info[j][i]

        if is_possible(road):
            res += 1
        # print(i)
    print('#{} {}'.format(test_case, res))
