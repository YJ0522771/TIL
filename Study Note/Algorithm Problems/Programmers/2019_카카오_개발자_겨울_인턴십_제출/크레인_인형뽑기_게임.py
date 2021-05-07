def solution(board, moves):
    answer = 0
    N = len(board)
    
    stack = []
    for m in moves:
        m -= 1
        for i in range(N):
            if board[i][m] == 0:
                continue
                
            if len(stack) and stack[len(stack) - 1] == board[i][m]:
                stack.pop()
                answer += 2
                board[i][m] = 0
            else:
                stack.append(board[i][m])
                board[i][m] = 0
            break
        # print(stack)
    
    return answer