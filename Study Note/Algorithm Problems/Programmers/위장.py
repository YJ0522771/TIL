def solution(clothes):
    answer = 1
    dic = {}
    
    for clothe in clothes:
        if clothe[1] not in dic.keys():
            dic[clothe[1]] = [clothe[0]]
        else:
            dic[clothe[1]].append(clothe[0])
            
    print(dic)
    
    for k in dic.keys():
        answer *= (len(dic[k]) + 1)
        
    answer -= 1
        
    return answer