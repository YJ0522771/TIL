import sys
sys.stdin = open("input.txt", "r")

costs = [0]
for i in range(1, 22):
    costs.append((i * i) + (i - 1) * (i - 1))


def search(r, c):
    ret = -1
    count = 0
    visit = [[0] * N for _ in range(N)]
    for k in range(1, N + 1 + is_even):
        for i in range(k):
            for d in delta:
                nr = r + d[0] * i
                nc = c + d[1] * (k - 1 - i)
                if is_in(nr, nc) and not visit[nr][nc]:
                    visit[nr][nc] = 1
                    if info[nr][nc]:
                        count += 1
        if costs[k] <= count * M:
            ret = count
        # print(k)
        # for i in range(N):
        #     print(visit[i])
        # print()
    return ret


def is_in(r, c):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True


delta = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    is_even = 1 if N % 2 == 0 else 0

    # search(4, 4)

    res = 0
    for r in range(N):
        for c in range(N):
            temp = search(r, c)
            if temp > res:
                res = temp

    print('#{} {}'.format(test_case, res))