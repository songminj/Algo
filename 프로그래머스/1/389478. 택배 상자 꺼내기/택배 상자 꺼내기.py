def solution(n, w, num):
    h = n//w + 1
    arr = []
    
    def picking(x, y):
        ans = 0 
        for i in range(x, h):
            if arr[i][y] <= n:
                ans += 1
            else:
                break
        return ans
    
    for i in range(h):
        if i % 2 == 0:
            arr.append([j for j in range(i*w+1,i*w+w+1)])
        else: 
            arr.append([j for j in range(i*w+w, i*w,-1)])
            
    for i in range(h):
        for j in range(w):
            if arr[i][j] == num:
                return picking(i, j)