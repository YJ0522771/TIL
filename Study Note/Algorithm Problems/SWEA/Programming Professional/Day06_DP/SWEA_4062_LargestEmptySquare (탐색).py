import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    N = int(input())
    image = [list(map(int, list(input()))) for _ in range(N)]

    black = []
    rows = [0]
    cols = [0]
    for i in range(N):
        for j in range(N):
            if image[i][j]:
                black.append((i, j))
                if i < N + 1:
                    rows.append(i + 1)
                if j < N + 1:
                    cols.append(j + 1)
    rows = set(sorted(rows))
    cols = set(sorted(cols))
    for k in range(N, 0, -1):
        for r in rows:
            if r + k - 1 >= N:
                break
            for c in cols:
                if c + k - 1 >= N:
                    break
                # print(r, c, k)
                state = True
                for b in black:
                    i, j = b[0], b[1]
                    if r <= i and r + k - 1 >= i and c <= j and c + k - 1 >= j:
                        # print(i, j)
                        state = False
                        break
                if state:
                    break
            if state:
                break
        if state:
            break
    print('#{} {}'.format(test_case, k))


