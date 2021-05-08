def solve(k):
    global N
    global M
    global cases
    global visit
    global results
    global res
    
    if k == M:
        if visit not in results:
            results.append(list(visit))
            res += 1
        return
    
    for i in range(N):
        if cases[k][i] and not visit[i]:
            visit[i] = True
            solve(k + 1)
            visit[i] = False
    return

res = 0
N = 0
M = 0
cases = []
visit = []
results = []
def solution(user_id, banned_id):
    global N
    global M
    global cases
    global visit
    
    answer = 1
    N = len(user_id)
    M = len(banned_id)
    
    print(user_id)
    print(banned_id)

    for ban in banned_id:
        temp = []
        for user in user_id:
            if len(user) != len(ban):
                temp.append(False)
                continue
                
            state = True
            for i in range(len(ban)):
                if ban[i] != '*' and ban[i] != user[i]:
                    state = False
                    break
                    
            temp.append(state)
        cases.append(temp)
    
    visit = [False] * N
    solve(0)
    # print(res)
    answer = res
        
    return answer