def solution(numbers):
    answer = ''
    nums = list(map(str, numbers))
    nums.sort(key=lambda x: x * 3, reverse=True)
    
    for n in nums:
        answer += n
        
    answer = str(int(answer))
        
    return answer