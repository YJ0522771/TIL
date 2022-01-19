def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    while citations[answer] >= answer + 1:
        answer += 1
        if answer == len(citations):
            break
    
    return answer