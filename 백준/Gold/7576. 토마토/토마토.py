import sys
from collections import deque
# m : 가로 n : 세로
m, n = map(int, sys.stdin.readline().strip().split())
tomato = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# 썩은 토마토 찾기
def rotten(tomato, rottens):
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                rottens.append((i, j))

def bfs(rottens):
    queue = deque()
    queue.extend(rottens)
    max_day = 0
    visited = [[False]* m for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if (0<= ni < n and 0 <= nj < m) and tomato[ni][nj] == 0 and not visited[ni][nj]:
                tomato[ni][nj] = tomato[x][y] + 1
                queue.append((ni, nj))

    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return -1
            elif max_day < tomato[i][j]:
                max_day = tomato[i][j]-1
    return max_day


rottens = []
rotten(tomato, rottens)
print(bfs(rottens))
