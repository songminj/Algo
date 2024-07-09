# 16234번 인구이동

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]


day = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(i, j):
    global arr
    queue = deque()
    queue.append((i, j))
    cnt = arr[i][j]
    visited[i][j] = True
    res = [(i, j)]
    while queue:
        x, y = queue.popleft()
        now = arr[x][y]
        for k in range(4):
            di = x + delta[k][0]
            dj = y + delta[k][1]
            if 0 <= di < N and 0 <= dj < N and not visited[di][dj]:
                if L <= abs(now - arr[di][dj]) <= R:
                    visited[di][dj] = True
                    queue.append((di, dj))
                    res.append((di, dj))
                    cnt += arr[di][dj]
    for x, y in res:
        arr[x][y] = cnt // len(res)
    return

while True:
    visited = [[False] * N for _ in range(N)]
    n = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j)
                n += 1
    if n == N**2:
        break
    day += 1
print(day)