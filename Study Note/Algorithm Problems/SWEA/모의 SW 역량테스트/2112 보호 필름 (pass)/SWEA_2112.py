import sys
sys.stdin = open("input.txt", "r")


def solve(k, cur, new_film):
    global res
    if is_OK(new_film):
        if cur < res:
            res = cur
        return

    if k == D or cur >= res:
        return

    temp = [0] * D
    for j in range(D):
        temp[j] = list(new_film[j])
    # k층에 약품을 안 넣을 때
    solve(k + 1, cur, temp)
    # k층에 A 약품을 넣을 때
    temp[k] = [0] * W
    solve(k + 1, cur + 1, temp)
    # k층에 B 약품을 넣을 때
    temp[k] = [1] * W
    solve(k + 1, cur + 1, temp)
    return


def is_OK(new_film):
    for i in range(W):
        count = 1
        OK = False
        for j in range(D - 1):
            if new_film[j][i] == new_film[j + 1][i]:
                count += 1
                if count >= K:
                    OK = True
                    break
            else:
                count = 1
        if not OK:
            return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////////
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    if K == 1:
        print('#{} 0'.format(test_case))
        continue

    res = D
    solve(0, 0, film)
    print('#{} {}'.format(test_case, res))
