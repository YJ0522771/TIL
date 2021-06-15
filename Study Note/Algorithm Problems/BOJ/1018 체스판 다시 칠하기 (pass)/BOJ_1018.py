def solve(r, c):
    res = N * M
    for t in range(2):
        temp = 0
        for i in range(8):
            k = t + i
            k %= 2
            for j in range(8):
                if board[r + i][c + j] != test[k][j]:
                    temp += 1
        if res > temp:
            res = temp

    return res


N, M = map(int, input().split())
board = [input() for _ in range(N)]

test = ['WBWBWBWB', 'BWBWBWBW']
res = N * M

for i in range(N - 7):
    for j in range(M - 7):
        temp = solve(i, j)
        if res > temp:
            res = temp

print(res)