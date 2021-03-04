import sys
sys.stdin = open("input.txt", "r")


def BFS(s, g):
    visit = [[0] * N for _ in range(N)]
    visit[s[0]][s[1]] = 1
    queue = [s]
    while len(queue):
        r, c = queue.pop(0)
        for j in range(4):
            nr = r + delta[j][0]
            nc = c + delta[j][1]
            if (nr, nc) == g:
                return 1
            if is_in(nr, nc) and maze[nr][nc] != 1 and not visit[nr][nc]:
                visit[nr][nc] = visit[r][c] + 1
                queue.append((nr, nc))
    return 0


def is_in(r, c):
    return r >= 0 and r < N and c >= 0 and c < N


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = 10
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////////////////
    N = int(input())
    N = 100
    maze = []
    for i in range(N):
        maze.append(list(map(int, list(input()))))
        if 2 in maze[i]:
            S = (i, maze[i].index(2))
        if 3 in maze[i]:
            G = (i, maze[i].index(3))


    print('#{} {}'.format(test_case, BFS(S, G)))