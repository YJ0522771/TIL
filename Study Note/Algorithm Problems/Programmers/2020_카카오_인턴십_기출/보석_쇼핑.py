def solution(gems):
    answer = [1, len(gems)]
    num = len(set(gems))
    temp = []
    dic = {}
    l = -1
    r = -1
    
    while l < len(gems) and r < len(gems):
        if len(dic) < num:
            r += 1
            if r == len(gems):
                break
            if gems[r] not in dic.keys():
                dic[gems[r]] = 1
            else:
                dic[gems[r]] += 1

        else:
            l += 1
            if l == len(gems):
                break
            temp.append([l + 1, r + 1])
            dic[gems[l]] -= 1
            if dic[gems[l]] == 0:
                del dic[gems[l]]
            
    temp.sort(key=lambda x: (x[1] - x[0], x[0]))

    answer = temp[0]
    return answer