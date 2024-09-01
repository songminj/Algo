# 1389번 케빈 베이컨의 6단계 법칙

import sys
from collections import deque
input = sys.stdin.readline

def kevin_beacon(k):
    global visited
    queue = deque([k])
    visited[k] = 1
    while queue:
        x = queue.popleft()
        for y in adj_d[x]:
            if not visited[y]:
                visited[y] = visited[x] + 1
                queue.append(y)

n, m = map(int, input().strip().split())
adj_d = {i: [] for i in range(1, n + 1)}
val = []

# 인접 리스트 생성
for i in range(m):
    s, e = map(int, input().strip().split())
    adj_d[s].append(e)
    adj_d[e].append(s)
for i in range(1, n + 1):
    visited = [0] * (n+1)
    kevin_beacon(i)
    val.append(sum(visited))
print(val.index(min(val)) + 1)