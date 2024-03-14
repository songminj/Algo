import sys
from collections import deque
n, m = map(int, sys.stdin.readline().strip().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        now_y, now_x = queue.popleft()
        for i in range(4):
            ni = now_y + di[i]
            nj = now_x + dj[i]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and arr[ni][nj] == '1':
                visited[ni][nj] = visited[now_y][now_x] + 1
                queue.append((ni, nj))

    return visited[n-1][m-1]
print(bfs(0, 0))
