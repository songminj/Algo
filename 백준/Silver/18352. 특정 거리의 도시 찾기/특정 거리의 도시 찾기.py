# 18352번 특정 거리의 도시 찾기

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())
dist = [0] * (N+1)

adj = {i : [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().strip().split())
    adj[a].append(b)

def bfs(X, K):
    queue = deque([X])
    dist = [-1] * (N+1)
    dist[X] = 0

    while queue:
        now = queue.popleft()
        for nxt in adj[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now]+1
                queue.append(nxt)
    res = [ i for i in range(1, N+1) if dist[i] == K]
    return res

result = bfs(X, K)

if result:
    print("\n".join(map(str, sorted(result))))
else:
    print(-1)