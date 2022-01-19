def solution(answers):
    answer = []
    p1 = []
    p2 = []
    p3 = []
    
    for i in range(1, 10001):
        temp = i % 5
        if temp:
            p1.append(temp)
        else:
            p1.append(5)
        
        temp = i % 2
        if temp:
            p2.append(2)
        else:
            temp = (i // 2) - 1
            temp = temp % 4
            p2.append(temp + 2 if temp else 1)
        
        temp = (i - 1) // 2
        temp = temp % 5
        if temp == 0:
            p3.append(3)
        elif temp >= 3:
            p3.append(temp + 1)
        else:
            p3.append(temp)

    i = 0
    count = [0, 0, 0]
    while i < len(answers):
        if answers[i] == p1[i]:
            count[0] += 1
        if answers[i] == p2[i]:
            count[1] += 1
        if answers[i] == p3[i]:
            count[2] += 1
        i += 1
        
    m = max(count)
    
    for i in range(3):
        if count[i] == m:
            answer.append(i + 1)
    
    return answer