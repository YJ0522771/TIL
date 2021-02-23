import sys
sys.stdin = open("input.txt", "r")


def search(adj, S, G):
    visit = [0] * 100
    return DFS(adj, visit, S, G)


def DFS(adj, visit, s, g):
    visit[s] = 1
    if s == g:
        return True
    for i in range(100):
        if adj[s][i] and not visit[i]:
            if DFS(adj, visit, i, g):
                return True
    return False


T = 10
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, E = map(int, input().split())
    adj = [[0] * 100 for _ in range(100)]
    edges = list(map(int, input().split()))
    for i in range(E):
        s, g = edges[2 * i], edges[2 * i + 1]
        adj[s][g] += 1
    S, G = 0, 99
    print('#{} {}'.format(test_case, int(search(adj, S, G))))