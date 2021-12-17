def solution(genres, plays):
    answer = []
    genre_cnt = {}
    genre_dic = {}
    
    for i in range(len(plays)):
        if genres[i] not in genre_cnt.keys():
            genre_cnt[genres[i]] = plays[i]
            genre_dic[genres[i]] = [[i, plays[i]]]
        else:
            genre_cnt[genres[i]] += plays[i]
            genre_dic[genres[i]].append([i, plays[i]])
        
    genre = []    
    for k in genre_cnt.keys():
        genre.append([k, genre_cnt[k]])
    genre.sort(key=lambda x: -x[1])
    
    for g in genre_dic.keys():
        genre_dic[g].sort(key=lambda x: -x[1])
        
    print(genre)
    print(genre_dic)
    
    for g in genre:
        temp = genre_dic[g[0]]
        answer.append(temp[0][0])
        if len(temp) >= 2:
            answer.append(temp[1][0])
        
    return answer