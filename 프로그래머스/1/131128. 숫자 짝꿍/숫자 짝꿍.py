def solution(X, Y):
    answer = ''
    x_num = [0] * 10
    y_num = [0] * 10
    
    for x in X:
        x_num[int(x)] += 1
    for y in Y:
        y_num[int(y)] += 1
    
    res_num = [0] * 10
    for i in range(10):
        res_num[i] = min(x_num[i], y_num[i])
    
    for i in range(9, -1, -1):
        if res_num[i] == 0:
            continue
        if i == 0 and answer == '':
            answer = '0'
            continue
        answer += (str(i)*res_num[i])
        
    return "-1" if answer == '' else answer