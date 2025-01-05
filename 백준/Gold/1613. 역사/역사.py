# 1613번 역사

import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
dist = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().strip().split())
    # a -> b 순서
    dist[a][b] = -1
    dist[b][a] = 1

# 플로이드-워셜
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] == -1 and dist[k][j] == -1:
                dist[i][j] = -1
                dist[j][i] = 1

s = int(input())
for _ in range(s):
    x, y = map(int, input().strip().split())
    print(dist[x][y])