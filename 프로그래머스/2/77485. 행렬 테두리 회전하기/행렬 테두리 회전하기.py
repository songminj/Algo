from pprint import pprint as pp

def solution(rows, columns, queries):
    answer = []
    arr = [[(i * columns + j + 1) for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = map(lambda x: x-1, query)
        curr = arr[x1][y1]
        min_val = curr
        
        # 윗줄밀기
        for i in range(y1+1, y2+1):
            arr[x1][i], curr = curr, arr[x1][i]
            min_val = min(curr, min_val)
        # 오른쪽줄 밀기 
        for i in range(x1+1, x2+1):
            arr[i][y2], curr = curr, arr[i][y2]
            min_val = min(curr, min_val)
        # 아랫줄 밀기 
        for i in range(y2-1,y1-1, -1):
            arr[x2][i], curr = curr, arr[x2][i]
            min_val = min(curr, min_val)
            
        # 왼쪽줄 밀기 
        for i in range(x2-1,x1-1, -1):
            arr[i][y1], curr = curr, arr[i][y1]
            min_val = min(curr, min_val)     
        answer.append(min_val)
    return answer