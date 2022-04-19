# 그래프

def solution(n, edge):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
        
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    distance = [0] * (n + 1)
    
    # bfs
    queue = [1]
    while len(queue):
        q = queue.pop(0)
        for e in graph[q]:
            if distance[e] or e == 1:
                continue
            distance[e] = distance[q] + 1
            queue.append(e)
            
    # print(distance)
    m = max(distance)
    
    answer = distance.count(m)
    return answer