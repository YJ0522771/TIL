import sys
sys.stdin = open("input.txt", "r")

queue = [0] * 1000001
count = [0] * 1000001
T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    check = [False] * 1000001
    f, t = 0, 0
    queue[t] = N
    count[t] = 0
    check[N] = True
    t += 1
    res = 0

    while f < t:
        q = queue[f]
        c = count[f]
        f += 1

        c += 1
        arr = [q + 1, q - 1, 2 * q, q - 10]
        for a in arr:
            if a == M:
                res = c
                break
            elif 0 < a <= 1000000 and not check[a]:
                queue[t] = a
                count[t] = c
                check[a] = True
                t += 1
        if res:
            break

    print('#{} {}'.format(test_case, res))