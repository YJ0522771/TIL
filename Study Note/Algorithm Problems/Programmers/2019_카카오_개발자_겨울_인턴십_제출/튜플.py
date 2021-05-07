def solution(s):
    answer = []
    s = s[1:len(s) - 1]
    s = s.split('},{')
    for i in range(len(s)):
        if s[i][0] == '{':
            s[i] = s[i][1:]
        if s[i][len(s[i]) - 1] == '}':
            s[i] = s[i][:len(s[i]) - 1]
            
        s[i] = list(map(int, s[i].split(',')))
        
    s.sort(key=lambda x: len(x))
    # print(s)
    for ss in s:
        for i in ss:
            if i not in answer:
                answer.append(i)
                break

    return answer