def solution(targets):
    answer, curr = 0, 0
    targets.sort(key = lambda x: x[1])
    n = len(targets)
    for i in range(n):
        if curr > targets[i][0]:
            continue
        curr = targets[i][1]
        answer += 1
            
    return answer