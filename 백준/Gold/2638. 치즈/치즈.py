# 2638번 치즈

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

chz = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            chz += 1

time = 0
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if 0 <= dx < N  and 0 <= dy < M:
                if not arr[dx][dy] and not visited[dx][dy]:
                    queue.append((dx, dy))
                    visited[dx][dy] = 1
                elif arr[dx][dy]:
                    visited[dx][dy] += 1

while True:
    visited = [[0] * M for _ in range(N)]
    bfs()
    time += 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                arr[i][j] = 0
                chz -=1
    if chz == 0:
        break
print(time)