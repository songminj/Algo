def solution(park, routes):
    d = {'N': (-1, 0), 'S': (1, 0), 'W':(0, -1), 'E':(0, 1)}
    curr = [0, 0]
    h, w = len(park), len(park[0])
        
    # 초기지점 찾기 
    for i in range(h):
        for j in range(w):
            if park[i][j] =='S':
                curr = [i, j]
                break
    
    # 이동시키기 
    for r in routes:
        op, n = r.split()
        n = int(n)
        
        can_move = True
        
        for i in range(1, n + 1):
            ni = curr[0] + d[op][0] * i
            nj = curr[1] + d[op][1] * i
            
            # 2. 경계 검사 및 장애물 검사
            if not (0 <= ni < h and 0 <= nj < w) or park[ni][nj] == 'X':
                can_move = False
                break
        
        if can_move:
            curr = [ni, nj]
    
    return curr