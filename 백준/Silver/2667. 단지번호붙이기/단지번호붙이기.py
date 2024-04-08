import sys

input = sys.stdin.readline

from collections import deque
from heapq import heappush, heappop

N =int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(i, j):
    global visited
    cnt = 0
    queue = deque()
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        cnt += 1
        visited[x][y] = True
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 1 and not visited[nx][ny] and (nx, ny) not in queue:
                    queue.append((nx, ny))
    return cnt

res, houses =0, []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            res += 1
            heappush(houses, bfs(i, j))
print(res)
for i in range(res):
    print(heappop(houses))