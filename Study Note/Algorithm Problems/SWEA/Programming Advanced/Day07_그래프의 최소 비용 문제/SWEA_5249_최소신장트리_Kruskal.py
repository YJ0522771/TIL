import sys
sys.stdin = open("input.txt", "r")

# Kruskal


def get_parent(x):
    if x == parent[x]:
        return x
    else:
        return get_parent(parent[x])


T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////////
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        e = tuple(map(int, input().split()))
        edges.append(e)

    edges.sort(key=lambda x: -x[2])
    # print(edges)

    parent = [i for i in range(V + 1)]
    count = 0
    res = 0
    while count < V:
        e = edges.pop()
        p1 = get_parent(e[0])
        p2 = get_parent(e[1])
        if p1 == p2:
            continue

        if p2 < p1:
            p1, p2 = p2, p1
        parent[p2] = parent[p1]
        # print(e)
        count += 1
        res += e[2]

    print('#{} {}'.format(test_case, res))