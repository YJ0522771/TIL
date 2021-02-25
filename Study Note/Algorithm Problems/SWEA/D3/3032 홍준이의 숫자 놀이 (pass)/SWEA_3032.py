import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ////////////////////////////////////////////////////////////
    A, B = map(int, input().split())
    s = [1, 0]
    t = [0, 1]
    reverse = False
    if A < B:
        A, B = B, A
        reverse = True
    r = [A, B]
    while True:
        ri = r[len(r) - 2] % r[len(r) - 1]
        if ri == 0:
            break
        q = r[len(r) - 2] // r[len(r) - 1]
        s.append(s[len(s) - 2] - s[len(s) - 1] * q)
        t.append(t[len(t) - 2] - t[len(t) - 1] * q)
        r.append(ri)

    if r[len(r) - 1] == 1:
        if reverse:
            print('#{} {} {}'.format(test_case, t[len(t) - 1], s[len(s) - 1]))
        else:
            print('#{} {} {}'.format(test_case, s[len(s) - 1], t[len(t) - 1]))
    else:
        print('#{} -1'.format(test_case))
