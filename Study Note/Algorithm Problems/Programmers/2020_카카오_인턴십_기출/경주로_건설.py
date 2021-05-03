def is_in(r, c, N):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False
    return True

def solution(board):
    answer = 0
    N = len(board)
    MAX = 1000000
    delta = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
    
    cost = [[MAX] * N for _ in range(N)]
    cost[0][0] = 0
    queue = []
    if board[0][1] == 0:
        cost[0][1] = 100
        queue.append((0, 1, 0, 100))
    if board[1][0] == 0:
        cost[1][0] = 100
        queue.append((1, 0, 1, 100))
    
    while len(queue):
        q = queue.pop(0)
        for i in range(1, 5):
            nr = q[0] + delta[i][0]
            nc = q[1] + delta[i][1]
            
            if is_in(nr, nc, N) and board[nr][nc] == 0:
                temp = q[3] + 100
                if (i % 2) != q[2]:
                    temp += 500
                
                if temp <= cost[nr][nc]:
                    cost[nr][nc] = temp
                    queue.append((nr, nc, i % 2, temp))
                    # print(nr, nc, i)
                    
    # for i in range(N):
    #     print(cost[i])
    # print(cost[N - 1][N - 1])
    if cost[N - 1][N - 1] != MAX:
        answer = cost[N - 1][N - 1]
    
    return answer