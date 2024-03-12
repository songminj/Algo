import sys
sys.setrecursionlimit(10**8)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dfs(i, j):
    global size
    visited[i][j] = True
    size += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0<= nj < m and arr[ni][nj] == '1' and not visited[ni][nj]:
            dfs(ni, nj)

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip().split()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        size = 0
        if arr[i][j] == '1' and not visited[i][j]:
            dfs(i, j)
            if max_size < size:
                max_size = size
            cnt += 1
print(cnt)
print(max_size)