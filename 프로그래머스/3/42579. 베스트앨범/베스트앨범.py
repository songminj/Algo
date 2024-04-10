from heapq import heappush, heappop

def solution(genres, plays):
    dic = {i : [] for i in list(set(genres))}
    
    # 정렬하면서 담음 (수록기준 2번)
    for i in range(len(genres)):
        dic[genres[i]].append((plays[i], i))
    # print(dic)
    
    # 수록기준 1번 
    order_type, idx = [], 0
    for key in dic.keys():
        order_type.append((key, sum(dic[key][i][0] for i in range(len(dic[key])))))
    order_type.sort(key = lambda x : x[1], reverse= True)
    answer = []
    # print(order_type)
    # 1번 기준 
    for t in order_type:
        genre = t[0]
        tmp = sorted(dic[genre], reverse=True)
        if len(tmp) >= 2:
            if tmp[0][0] == tmp[1][0]:
                answer.extend([min(tmp[0][1], tmp[1][1]), max(tmp[0][1], tmp[1][1])])
            else:
                for i in range(2):
                    answer.append(tmp[i][1])
        else:
            answer.append(tmp[0][1])
        
        

    return answer