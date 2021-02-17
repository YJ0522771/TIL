import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    graph = [0]
    for i in range(N):
        graph.append([])
    for i in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
    for i in range(1, N):
        graph[i].sort()
        
    count = 0
    for i in range(1, N):
        for j in range(len(graph[i])):
            for e in graph[graph[i][j]]:
                for k in range(j + 1, len(graph[i])):
                    if e == graph[i][k]:
                        count += 1
    print('#{} {}'.format(test_case, count))