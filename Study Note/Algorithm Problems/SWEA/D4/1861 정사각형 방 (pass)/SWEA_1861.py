import sys
sys.stdin = open("input.txt", "r")


def solve(r, c, count):
    mm = 0
    for d in delta:
        nr = r + d[0]
        nc = c + d[1]
        if is_in(nr, nc) and rooms[nr][nc] == rooms[r][c] + 1:
            temp = solve(nr, nc, count + 1)
            if temp > mm:
                mm = temp
    return mm if mm else count


def is_in(r, c):
    if r < 1 or r > N or c < 1 or c > N:
        return False
    return True


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////
    N = int(input())
    rooms = [[0] * (N + 1)]
    for _ in range(N):
        rooms.append([0] + list(map(int, input().split())))

    # path = [[0] * (N + 1) for _ in range(N + 1)]
    res = 0
    room = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            temp = solve(i, j, 1)
            if res < temp:
                res = temp
                room = rooms[i][j]
            elif res == temp and room > rooms[i][j]:
                room = rooms[i][j]

    print('#{} {} {}'.format(test_case, room, res))