import sys
import datetime
flie = open("5293_DFS(8).txt", "w")
current_time = datetime.datetime.now()
limit = 8

case = [[[[0] * limit for _ in range(limit)] for _ in range(limit)] for _ in range(limit)]
case[1][0][0][0] = '00'
case[0][1][0][0] = '01'
case[0][0][1][0] = '10'
case[0][0][0][1] = '11'
start = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1)
]
delta = [
    [ [1, 0, 0, 0], [0, 1, 0, 0] ],
    [ [0, 0, 1, 0], [0, 0, 0, 1] ]
]

last = []
stack = []
for k in range(4):
    last.append(k % 2)
    stack.append(start[k])
    l = last.pop()
    A, B, C, D = stack.pop()

    while True:
        n = case[A][B][C][D]
        if l == 0: # 맨 마지막이 A, C일 때
            temp = tuple([e + delta[l][0][i] for i, e in enumerate([A, B, C, D])])
            a, b, c, d = temp
            if limit not in temp:
                stack.append(temp)
                last.append(0)
                if not case[a][b][c][d]:
                    case[a][b][c][d] = n + '0'
            temp = tuple([e + delta[l][1][i] for i, e in enumerate([A, B, C, D])])
            a, b, c, d = temp
            if limit not in temp:
                stack.append(temp)
                last.append(1)
                if not case[a][b][c][d]:
                    case[a][b][c][d] = n + '1'
        elif l == 1: # B, D일 때
            temp = tuple([e + delta[l][0][i] for i, e in enumerate([A, B, C, D])])
            a, b, c, d = temp
            if limit not in temp:
                stack.append(temp)
                last.append(0)
                if not case[a][b][c][d]:
                    case[a][b][c][d] = n + '0'
            temp = tuple([e + delta[l][1][i] for i, e in enumerate([A, B, C, D])])
            a, b, c, d = temp
            if limit not in temp:
                stack.append(temp)
                last.append(1)
                if not case[a][b][c][d]:
                    case[a][b][c][d] = n + '1'

        if not len(stack):
            break
        
        A, B, C, D = stack.pop()
        l = last.pop()

        # print(k+1, len(queue))
        # print(A, B, C, D)
        # print(case[A][B][C][D])

    print('{} end : {}'.format(k + 1, datetime.datetime.now() - current_time))
flie.write(str(case))
flie.close()