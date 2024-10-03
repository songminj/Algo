# 5567번 결혼식

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([(1, 0)])
    visited = [False] * (N+1)
    visited[1] = True
    cnt = 0
    while queue:
        x, r = queue.popleft()
        for v in friend[x]:
            if not visited[v] and r < 2:
                visited[v] = True
                queue.append((v, r+1))
                cnt += 1
    print(cnt)

N = int(input())
M = int(input())
friend = { i : [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().strip().split())
    friend[a].append(b)
    friend[b].append(a)

bfs()