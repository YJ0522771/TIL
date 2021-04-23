import sys
sys.stdin = open("input.txt", "r")


def get_parent(x):
    if x == parent[x]:
        return x
    else:
        return get_parent(parent[x])


T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        pa = get_parent(a)
        pb = get_parent(b)
        if pa > pb:
            pa, pb = pb, pa
        parent[pb] = pa

    visit = [False] * (N + 1)
    res = 0
    for i in range(1, N + 1):
        p = get_parent(i)
        if not visit[p]:
            visit[p] = True
            res += 1

    print('#{} {}'.format(test_case, res))