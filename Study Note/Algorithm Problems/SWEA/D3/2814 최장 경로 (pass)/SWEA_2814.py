import sys
sys.stdin = open("input.txt", "r")

def search(adj, N, visit, count, V):
    max_count = count
    for i in range(1, N + 1):
        if adj[V][i] and not visit[i]:
            visit[i] = 1
            temp = search(adj, N, visit, count + 1, i)
            visit[i] = 0
            if max_count < temp:
                max_count = temp
    return max_count

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x][y] += 1
        adj[y][x] += 1
    max_dep = 0
    for i in range(1, N + 1):
        visit = [0] * (N  + 1)
        visit[i] = 1
        d = search(adj, N, visit, 1, i)
        print(i, d)
        if max_dep < d:
            max_dep = d
    print('#{} {}'.format(test_case, max_dep))
