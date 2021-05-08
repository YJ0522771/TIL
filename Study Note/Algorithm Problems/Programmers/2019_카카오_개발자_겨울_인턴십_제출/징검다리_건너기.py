def solve(stones, k, x):
    count = 0
    mm = 0
    for s in stones:
        if s < x:
            count += 1
        else:
            if mm < count:
                mm = count
            count = 0
    
    if mm < count:
        mm = count
            
    if mm < k:
        return True
    else:
        return False
    
    
def solution(stones, k):
    answer = 0
    
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        tf = solve(stones, k, mid)
        if tf:
            left = mid + 1
        else:
            right = mid - 1
            
        # print(mid, tf)
    if tf:
        answer = mid
    else:
        answer = mid - 1
    
    return answer