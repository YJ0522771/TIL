import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    min_cnt = N * M
    for w in range(1, N - 1):
        for b in range(w + 1, N):
            count = 0
            for i in range(w):
                for s in flag[i]:
                    if s != 'W':
                        count += 1
            if min_cnt < count:
                break
            for i in range(w, b):
                for s in flag[i]:
                    if s != 'B':
                        count += 1
            if min_cnt < count:
                break
            for i in range(b, N):
                for s in flag[i]:
                    if s != 'R':
                        count += 1
            if min_cnt > count:
                min_cnt = count

    print('#{} {}'.format(test_case, min_cnt))

