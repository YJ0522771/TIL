import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output1.txt", "w")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = []
    for i in range(N):
        c_cnt = 0
        for j in range(N):
            if arr[i][j]:
                c_cnt += 1
            if c_cnt:
                if arr[i][j] == 0:
                    c = j - 1
                elif j == N - 1:
                    c = j
                else:
                    continue
                r_cnt = 0
                for k in range(i, N):
                    if arr[k][c]:
                        r_cnt += 1
                    else:
                        break
                res.append((r_cnt, c_cnt))
                for k in range(i, i + r_cnt):
                    for l in range(c - c_cnt + 1, c + 1):
                        arr[k][l] = 0
                c_cnt = 0

    for i in range(len(res) - 1, 0, -1):
        max_mat = 0
        max_index = 0
        for j in range(i + 1):
            temp = res[j][0] * res[j][1]
            if temp > max_mat:
                max_mat = temp
                max_index = j
            elif temp == max_mat and res[max_index][0] < res[j][0]:
                max_mat = temp
                max_index = j
        res[i], res[max_index] = res[max_index], res[i]

    print('#{} {}'.format(test_case, len(res)), end='')
    for i in range(len(res)):
        print(' {} {}'.format(res[i][0], res[i][1]), end='')
    print()


