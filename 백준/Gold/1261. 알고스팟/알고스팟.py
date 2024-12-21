# 1261번 알고스팟

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().strip().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
max_move = N+M-1
dist = [[max_move]*M for _ in range(N)]
dist[0][0] = 0

pq = deque([(0, 0)])

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

while pq:
    x, y = pq.popleft()
    for i in range(4):
        nx = x + di[i]
        ny = y + dj[i]
        if 0 <= nx < N  and 0 <= ny < M:
            # 0일 때
            if arr[nx][ny] == 0 and (dist[x][y] < dist[nx][ny]):
                dist[nx][ny] = dist[x][y]
                pq.appendleft((nx, ny))
            # 1일 때
            elif arr[nx][ny] == 1 and (dist[x][y]+1 < dist[nx][ny]):
                dist[nx][ny] = dist[x][y]+1
                pq.append((nx, ny))

print(dist[N-1][M-1])