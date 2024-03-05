# 쉬운 최단거리
"""
BFS와 DP를 한번에 사용한다
"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

area = [list(sys.stdin.readline().strip().split()) for _ in range(n)]



def bfs(a, b):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    queue.append((a, b))
    while queue:
        y, x = queue.popleft()
        if not visited[y][x] :
            visited[y][x] = True
            for i in range(4):
                ni = y + di[i]
                nj = x + dj[i]
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and area[ni][nj] == '1':
                    next = area[y][x] +1
                    area[ni][nj] = next
                    queue.append([ni, nj])
                    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and area[i][j] == '1':
                area[i][j] = -1

def find_start(area):
    for i in range(n):
        for j in range(m):
            if area[i][j] == '2':
                area[i][j] = 0
                return (i, j)


start = find_start(area)
bfs(start[0], start[1])

for i in range(n):
    print(*area[i])