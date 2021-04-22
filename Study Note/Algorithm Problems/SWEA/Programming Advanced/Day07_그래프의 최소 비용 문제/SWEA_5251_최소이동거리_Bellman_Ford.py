import sys
sys.stdin = open("input.txt", "r")

# Bellman-Ford

MAX = 10000000
T = int(input())
for test_case in range(1, T + 1):
    # /////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # /////////////////////////////////////////////////
    N, E = map(int, input().split())
    adj = [[MAX] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    D = [MAX] * (N + 1)
    visit = [False] * (N + 1)
    D[0] = 0

    queue = [0]
    count = 0
    while len(queue):
        q = queue.pop(0)

        ###################################################
        for i in range(N + 1):
            if q == i or adj[q][i] == MAX:
                continue

            if D[i] > D[q] + adj[q][i]:
                D[i] = D[q] + adj[q][i]
                # 최단경로 정보가 바뀌면 해당 노드를 거치는 모든 곳의 정보가 바뀐다.
                queue.append(i)
        ####################################################
        # print(q, D)

    print('#{} {}'.format(test_case, D[N]))