import sys
input = sys.stdin.readline

delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def dfs(x, y, t):
    global res
    if t > res:
        res = t
    for i in range(4):
        ni = x + delta[i][0]
        nj = y + delta[i][1]
        if 0 <= ni < r and 0 <= nj < c:
            word = ord(arr[ni][nj])-65
            if not visited[word]:
                visited[word] = 1
                dfs(ni, nj, t+1)
                visited[word] = 0

r, c = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(r)]
res = 1
visited = [False] * 26
visited[ord(arr[0][0])-65] = 1
dfs(0, 0, 1)
print(res)