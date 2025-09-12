# 1325 효율적인 해킹

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
graph = {i : [] for i in range(1, N+1)}
max_cnt = 0
res = []

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[b].append(a)

def bfs(x):
    visited = [False] * (N + 1)
    visited[x] = True

    queue = deque([x])
    while queue:
        node = queue.popleft()
        for x in graph[node]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True
    return sum(visited)

for i in range(1, N+1):
    cnt = bfs(i)
    if cnt == max_cnt:
        res.append(str(i))
    elif cnt > max_cnt:
        res = [str(i)]
        max_cnt = cnt

print(' '.join(res))