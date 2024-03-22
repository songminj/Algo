import sys
input = sys.stdin.readline

def paper(x, y, n):
    global white, blue
    tgt = arr[x][y]
    for i in range(x, n+x):
        for j in range(y, n+y):
            if arr[i][j] != tgt:
                paper(x, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y, n//2)
                paper(x+n//2, y+n//2, n//2)
                return
    else:
        if tgt == 0:
            white += 1
        else:
            blue += 1



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
paper(0, 0, n)
print(white, blue, sep='\n')
