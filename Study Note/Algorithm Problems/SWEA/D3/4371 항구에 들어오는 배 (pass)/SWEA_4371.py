import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////////////////////
    N = int(input())
    days = [int(input()) for _ in range(N)]
    last_day = days[N - 1]
    cal = []
    count = 0
    for d in days:
        if d == 1:
            cal.append(d)
            continue
        state = False
        for i in range(d, last_day + 1, d - 1):
            if i not in cal:
                state = True
                cal.append(i)
        cal.sort()
        if state:
            count += 1
        if cal == days:
            break

    print('#{} {}'.format(test_case, count))