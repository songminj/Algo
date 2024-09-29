# 14496 그대, 그머가 되어

import sys
from collections import deque
input = sys.stdin.readline

def find(a):
    queue = deque([(a, 0)])
    visited = [False] * (N+1)
    res = 10001
    while queue:
        now, cnt = queue.popleft()
        if now == b:
            res = min(res, cnt)
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, cnt+1))
    if res == 10001:
        return -1
    else:
        return res

# 머호가 바꾸려고 하는 문자 a, b
a, b = map(int, input().strip().split())
# 전체 문자수 N과 치환가능한 문자쌍 수 M
N, M = map(int, input().strip().split())
graph = {i : [] for i in range(1, N+1)}
res = 10001
for i in range(M):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N+1)
visited[a] = True

print(find(a))