import sys
sys.stdin = open("input.txt", "r")


def ccw(r, p, q):
    rp = (p[0] - r[0], p[1] - r[1])
    rq = (q[0] - r[0], q[1] - r[1])

    temp = rp[0] * rq[1] - rp[1] * rq[0]
    if temp >= 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):
    # //////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # //////////////////////////////////////////////
    N = int(input())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))

    points.sort(key=lambda x: (x[0], x[1]))

    visit = [False] * N
    stack = [0, 1]
    visit[0] = visit[1] = True

    # 위로 시계 방향 검사
    for i in range(N):
        if visit[i]:
            continue
        r = points[stack[len(stack) - 2]]
        p = points[stack[len(stack) - 1]]
        q = points[i]
        while ccw(r, p, q) >= 0 and len(stack) >= 2:
            s = stack.pop()
            visit[s] = False
            p = r
            r = points[stack[len(stack) - 2]]
        stack.append(i)
        visit[i] = True

    # 아래로 시계 방향 검사
    for i in range(N - 2, -1, -1):
        if visit[i] and i != 0:
            continue
        r = points[stack[len(stack) - 2]]
        p = points[stack[len(stack) - 1]]
        q = points[i]
        while ccw(r, p, q) >= 0 and len(stack) >= 2:
            s = stack.pop()
            visit[s] = False
            p = r
            r = points[stack[len(stack) - 2]]
        stack.append(i)
        visit[i] = True

    print('#{} {}'.format(test_case, len(stack) - 1))

