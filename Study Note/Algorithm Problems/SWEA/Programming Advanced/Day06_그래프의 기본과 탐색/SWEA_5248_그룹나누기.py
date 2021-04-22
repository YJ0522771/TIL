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
    nums = list(map(int, input().split()))

    parent = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = i

    for i in range(0, len(nums), 2):
        a, b = nums[i], nums[i + 1]
        pa = get_parent(a)
        pb = get_parent(b)
        if pb < pa:
            pa, pb = pb, pa
        parent[pb] = parent[pa]

        # parent[b] = parent[a]

    visit = [False] * (N + 1)
    res = 0
    for i in range(1, N + 1):
        p = get_parent(i)
        if not visit[p]:
            visit[p] = True
            res += 1

    # print(parent)
    print('#{} {}'.format(test_case, res))
