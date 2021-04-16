import sys
sys.stdin = open("input.txt", "r")

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////
    N = int(input())
    rooms = [[0] * (N + 2)]
    for _ in range(N):
        rooms.append([0] + list(map(int, input().split())) + [0])
    rooms.append([0] * (N + 2))

    path = [0] * (N * N + 1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for d in delta:
                if rooms[i][j] + 1 == rooms[i + d[0]][j + d[1]]:
                    path[rooms[i][j]] += 1
    # print(path)
    count = 0
    res = 0
    room = 0
    for i in range(len(path) - 1, -1, -1):
        if path[i]:
             count += 1
        else:
            if res <= count + 1:
                res = count + 1
                room = i + 1
            count = 0

    print('#{} {} {}'.format(test_case, room, res))
