# 11404번 플로이드

import sys
input = sys.stdin.readline
INF = int(10e9)
n = int(input())
m = int(input())
dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().strip().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if dist[a][b] == INF:
            print("0",  end=" ")
        else:
            print(dist[a][b], end=" ")
    print()