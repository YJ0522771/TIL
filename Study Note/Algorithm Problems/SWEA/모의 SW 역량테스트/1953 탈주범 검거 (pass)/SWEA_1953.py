import sys
sys.stdin = open("input.txt", "r")


def can_go(r, c, d):
    if r < 0 or r >= N or c < 0 or c >= M or visit[r][c]:
        return False
    t = m[r][c]
    if t == 0:
        return False
    if d == 1:
        if t not in [1, 2, 5, 6]:
            return False
    elif d == 2:
        if t not in [1, 2, 4, 7]:
            return False
    elif d == 3:
        if t not in [1, 3, 4, 5]:
            return False
    elif d == 4:
        if t not in [1, 3, 6, 7]:
            return False
    return True


delta = [
    [(0, 0)],
    [(-1, 0), (1, 0), (0, -1), (0, 1)],
    [(-1, 0), (1, 0)],
    [(0, -1), (0, 1)],
    [(-1, 0), (0, 1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)],
    [(-1, 0), (0, -1)]
]

direction = [
    [0],
    [1, 2, 3, 4],
    [1, 2],
    [3, 4],
    [1, 4],
    [2, 4],
    [2, 3],
    [1, 3]
]

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////
    N, M, R, C, L = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    queue = []
    queue.append((R, C))

    time = 1
    while time <= L:
        new_q = []
        while len(queue):
            r = queue[0][0]
            c = queue[0][1]
            queue.pop(0)
            visit[r][c] = time
            tp = m[r][c]
            dels = list(delta[tp])
            for i in range(len(dels)):
                nr = r + dels[i][0]
                nc = c + dels[i][1]
                if can_go(nr, nc, direction[tp][i]):
                    new_q.append((nr, nc))

        queue = list(new_q)
        time += 1

    res = 0
    for i in range(N):
        res += (M - visit[i].count(0))

    print('#{} {}'.format(test_case, res))
