import sys
import datetime
sys.stdin = open('input.txt', 'r')



def search_path():
    global path_state
    for core in cores:
        temp = []
        for i in range(4):
            nr = core[0] + delta[i][0]
            nc = core[1] + delta[i][1]
            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                temp.append(path(nr, nc, i, 0))
            else:
                temp.append(0)
        path_state.append(temp)


def path(r, c, direct, depth):
    if r < 0 or r >= N or c < 0 or c >= N:
        return depth
    if m[r][c] == 1:
        return 0
    nr = r + delta[direct][0]
    nc = c + delta[direct][1]
    return path(nr, nc, direct, depth + 1)


def solve(i, core_n, path_sum, connect):
    global res
    global res_con
    global visit
    if i == core_n:
        if connect > res_con:
            res = path_sum
            res_con = connect
        elif connect == res_con and res > path_sum:
            res = path_sum
        # print(path_sum, connect)
        return
    if path_sum > res and connect + (core_n - i) < res_con:
        return
    # if connect + (core_n - i) < res_con:
    #     print(i, connect, res_con)
    #     return
    c = cores[i]
    if c[0] == 0 or c[0] == N - 1 or c[1] == 0 or c[1] == N - 1:
        solve(i + 1, core_n, path_sum, connect + 1)
    else:
        pl = path_state[i]
        for j in range(4):
            if pl[j] == 0:
                # print(cores[i], '0')
                solve(i + 1, core_n, path_sum, connect)
                continue
            state = True
            nr = cores[i][0] + delta[j][0]
            nc = cores[i][1] + delta[j][1]
            while nr >= 0 and nr < N and nc >= 0 and nc < N:
                # print((nr, nc), visit[nr][nc])
                if visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    nr += delta[j][0]
                    nc += delta[j][1]
                else:
                    state = False
                    break
            if state:
                # print(cores[i], path_sum, pl[j], 'T')
                solve(i + 1, core_n, path_sum + pl[j], connect + 1)

            nr -= delta[j][0]
            nc -= delta[j][1]
            while nr != cores[i][0] or nc != cores[i][1]:
                visit[nr][nc] = 0
                nr -= delta[j][0]
                nc -= delta[j][1]
            if not state:
                # print(cores[i], 'F')
                solve(i + 1, core_n, path_sum, connect)


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for test_case in range(1, T + 1):
    start = datetime.datetime.today()
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if m[i][j]:
                cores.append((i, j))

    visit = [[0] * N for _ in range(N)]
    for c in cores:
        visit[c[0]][c[1]] = 1

    path_state = []
    search_path()
    # print(path_state)
    res = N * N
    res_con = 0
    # temp = []
    # for c in cores:
    #     if c[0] == 0 or c[0] == N - 1 or c[1] == 0 or c[1] == N - 1:
    #         temp.append(c)
    #         res_con += 1
    # for t in temp:
    #     cores.index(t)
    # print(cores)
    solve(0, len(cores), 0, res_con)
    # print(res, res_con)
    #

    print("#{} {}".format(test_case, res))

    print(datetime.datetime.today() - start)
