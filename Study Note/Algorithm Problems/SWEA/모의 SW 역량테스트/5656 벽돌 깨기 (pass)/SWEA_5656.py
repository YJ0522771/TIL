import sys
sys.stdin = open("input.txt", "r")


def solve(k, bb):
    global res
    if k == N:
        count = 0
        for i in range(H):
            for j in range(W):
                if bb[i][j]:
                    count += 1
        if res > count:
            res = count
        return

    tops = []
    for j in range(W):
        for i in range(H):
            if bb[i][j]:
                tops.append((i, j))
                break
    if len(tops) == 0:
        res = 0
        return

    for t in tops:
        # 벽돌 map 복사
        temp = []
        for i in range(H):
            temp.append(list(bb[i]))

        # 연쇄 폭발 : BFS
        queue = [t]
        while len(queue):
            q = queue.pop(0)
            for i in range(1, temp[q[0]][q[1]]):
                for d in delta:
                    nr = q[0] + d[0] * i
                    nc = q[1] + d[1] * i
                    if is_in(nr, nc) and temp[nr][nc]:
                        if temp[nr][nc] and (nr, nc) not in queue:
                            queue.append((nr, nc))
            temp[q[0]][q[1]] = 0

        # 아래에 빈 공간이 있는 벽돌 떨어뜨리기
        for j in range(W):
            for i in range(H - 1, -1, -1):
                if temp[i][j]:
                    y = i + 1
                    while True:
                        if y >= H or temp[y][j]:
                            break
                        temp[y][j], temp[y - 1][j] = temp[y - 1][j], temp[y][j]
                        y += 1

        solve(k + 1, temp)
    return


def is_in(r, c):
    if r < 0 or r >= H or c < 0 or c >= W:
        return False
    return True


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////
    N, W, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(H)]

    # for i in range(H):
    #     print(blocks[i])

    res = W * H + 10
    solve(0, blocks)
    print('#{} {}'.format(test_case, res))

