# 14502번 연구소

import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

blank, virus = [], []
# 벽 세울 수 있는 곳 찾기 / 바이러스 위치
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            blank.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    visited = [[False] * m for _ in range(n)]
    queue = deque(virus)
    for x, y in virus:
        visited[x][y] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + delta[i][0], y + delta[i][1]
            if 0 <= dx < n and 0 <= dy < m:
                if arr[dx][dy] == 0 and not visited[dx][dy]:
                    queue.append((dx, dy))
                    visited[dx][dy] = True
                    cnt += 1
    return cnt

len_blank = len(blank)
res = 0
for walls in combinations(blank, 3):
    for x, y in walls:
        arr[x][y] = 1
    infection = bfs()

    safe = len_blank - infection
    if safe > res:
        res = safe

    for x, y in walls:
        arr[x][y] = 0

print(res-3)