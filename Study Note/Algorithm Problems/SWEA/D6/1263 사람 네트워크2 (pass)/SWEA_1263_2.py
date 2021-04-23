import sys
sys.stdin = open("input.txt", "r")

MAX = 1000000
T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////
    input_data = list(map(int, input().split()))
    N = input_data[0]
    adj_k_1 = []
    for i in range(1, len(input_data), N):
        adj_k_1.append(input_data[i: i + N])

    for i in range(N):
        for j in range(N):
            if adj_k_1[i][j] == 0 and i != j:
                adj_k_1[i][j] = MAX

    # for i in range(N):
    #     print(adj_k_1[i])
    # print()

    adj_k = [[MAX] * N for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                adj_k[i][j] = min(adj_k_1[i][j], adj_k_1[i][k] + adj_k_1[k][j])

        # 매번 복사하는데 시간이 오래 걸린다.
        for i in range(N):
            adj_k_1[i] = list(adj_k[i])

    res = MAX
    for i in range(N):
        temp = sum(adj_k[i])
        if res > temp:
            res = temp
    print('#{} {}'.format(test_case, res))
