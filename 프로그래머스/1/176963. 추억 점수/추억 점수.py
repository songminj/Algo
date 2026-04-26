def solution(name, yearning, photo):
    n = len(name)
    set_name = set(name)
    scores = dict()
    for i in range(n):
        scores[name[i]] = scores.get(name[i], yearning[i])
    
    answer = []
    for ps in photo:
        cnt = 0
        for target in ps:
            if target in set_name:
                cnt += scores[target]
        answer.append(cnt)
        
    return answer