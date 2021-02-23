import sys
sys.stdin = open("input.txt", "r")

tank = ['^', 'v', '<', '>']
key = ['U', 'D', 'L', 'R']
move = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]
    N = int(input())
    user = list(input())
    current = 0
    for i in range(H):
        for j in range(W):
            t = field[i][j]
            if t in tank:
                if t == tank[0]:
                    current = key[0]
                elif t == tank[1]:
                    current = key[1]
                elif t == tank[2]:
                    current = key[2]
                else:
                    current = key[3]
                h, w = i, j
                break
        if current:
            break
    for u in user:
        if u == 'S':
            ph, pw = tuple(move[current])
            nh = h + ph
            nw = w + pw
            while (nh >= 0 and nh < H) and (nw >= 0 and nw < W):
                if field[nh][nw] == '*':
                    field[nh][nw] = '.'
                    break
                elif field[nh][nw] == '#':
                    break
                nh += ph
                nw += pw
        else:
            nh = h + move[u][0]
            nw = w + move[u][1]
            if (nh >= 0 and nh < H) and (nw >= 0 and nw < W) and field[nh][nw] == '.':
                field[h][w] = '.'
                h = nh
                w = nw
            field[h][w] = tank[key.index(u)]
            current = u
    print('#{} '.format(test_case), end='')
    for i in range(H):
        print(''.join(field[i]))
