import sys
sys.stdin = open("input.txt", "r")


def solve(x, y, depth, K_used, K_col):
    global res
    global visit
    global m
    # print((x, y), m[x][y], depth, res)
    is_end = True
    for de in delta:
        nx = x + de[0]
        ny = y + de[1]
        if is_in(nx, ny) and not visit[nx][ny]:
            if m[x][y] > m[nx][ny]:
                is_end = False
            elif m[x][y] > (m[nx][ny] - K) and (not K_used):
                is_end = False
                K_temp = m[nx][ny]
                K_col[0], K_col[1] = nx, ny
                m[nx][ny] = m[x][y] - 1
                K_used = True
                # print((nx, ny), K_used, m[nx][ny])
            else:
                continue
            visit[nx][ny] = 1
            solve(nx, ny, depth + 1, K_used, K_col)
            visit[nx][ny] = 0
            if K_used and K_col[0] == nx and K_col[1] == ny:
                K_used = False
                m[nx][ny] = K_temp
    if is_end:
        if res < depth:
            res = depth
        # print('end')


def is_in(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    return False


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    mm = []
    max_num = 0
    for _ in range(N):
        temp = list(map(int, input().split()))
        mm.append(temp)
        temp = max(temp)
        if temp > max_num:
            max_num = temp

    stack = []
    for i in range(N):
        for j in range(N):
            if mm[i][j] == max_num:
                stack.append((i, j))
    res = 0
    for s in stack:
        x = s[0]
        y = s[1]
        m = []
        for i in range(N):
            m.append(list(mm[i]))
        visit = [[0] * N for _ in range(N)]
        visit[x][y] = 1
        K_col = [-1, -1]
        solve(x, y, 0, False, K_col)
        # print()

    print('#{} {}'.format(test_case, res + 1))