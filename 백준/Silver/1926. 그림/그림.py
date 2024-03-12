import sys
from collections import deque
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i, j):
    size = 1
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        newi, newj = queue.popleft()
        for k in range(4):
            ni = newi + di[k]
            nj = newj + dj[k]
            if 0<= ni < n and 0 <= nj < m:
                if arr[ni][nj] == '1' and not visited[ni][nj]:
                    visited[ni][nj] = True
                    size += 1
                    queue.append((ni, nj))
    return size

n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip().split()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        size = 0
        if arr[i][j] == '1' and not visited[i][j]:
            max_size = max(bfs(i, j), max_size)
            cnt += 1
print(cnt)
print(max_size)