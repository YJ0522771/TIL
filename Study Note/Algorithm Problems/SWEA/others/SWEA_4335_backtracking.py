import sys
import datetime
sys.stdin = open("4335_input.txt", "r")

start = datetime.datetime.now()


def solve(w, d, cur_h):
    global visit
    global res

    if cur_h > res:
        res = cur_h
    else:
        temp = 0
        for i in range(N):
            if not visit[i]:
                temp += box_max[i]
        if res > cur_h + temp:
            return

    for i in range(N):
        if visit[i]:
            continue

        for j in range(3):
            for k in range(j + 1, 3):
                for l in range(3):
                    if l != j and l != k:
                        break
                if box[i][j] <= w and box[i][k] <= d:
                    visit[i] = True
                    solve(box[i][j], box[i][k], cur_h + box[i][l])
                    visit[i] = False
                elif box[i][k] <= w and box[i][j] <= d:
                    visit[i] = True
                    solve(box[i][k], box[i][j], cur_h + box[i][l])
                    visit[i] = False

    return res


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    box = []
    box_max = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        box.append((a, b, c))
        box_max.append(max([a, b, c]))

    visit = [False] * N

    res = 0
    for i in range(N):
        for j in range(3):
            for k in range(j + 1, 3):
                for l in range(3):
                    if l != j and l != k:
                        break
                visit[i] = True
                temp = solve(box[i][j], box[i][k], box[i][l])
                visit[i] = False
                if temp > res:
                    res = temp
    print('#{} {}'.format(test_case, res))
    print(datetime.datetime.now() - start)