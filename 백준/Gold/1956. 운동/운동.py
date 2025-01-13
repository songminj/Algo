# 1956번 운동

import sys
input = sys.stdin.readline

INF = 10**9

V, E = map(int, input().strip().split())
dist = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().strip().split())
    dist[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

val = INF

for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j :
            if dist[i][j] < INF and dist[j][i] < INF:
                val = min(val, dist[i][j]+dist[j][i])

if val == INF:
    print(-1)
else:
    print(val)