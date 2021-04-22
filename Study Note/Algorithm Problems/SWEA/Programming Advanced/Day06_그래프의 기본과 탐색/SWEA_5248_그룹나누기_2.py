import sys
sys.stdin = open("input.txt", "r")

# BFS

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    visit = [False] * (N + 1)

    adj = [[False] * (N + 1) for _ in range(N + 1)]
    for i in range(0, len(nums), 2):
        a, b = nums[i], nums[i + 1]
        adj[a][b] = adj[b][a] = True

    res = 0
    for i in range(1, N + 1):
        if not visit[i]:
            queue = [i]
            while len(queue):
                q = queue.pop(0)
                for i in range(1, N + 1):
                    if adj[q][i] and not visit[i]:
                        visit[i] = True
                        queue.append(i)
            res += 1

    print('#{} {}'.format(test_case, res))
