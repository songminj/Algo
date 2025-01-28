# 1922번 네트워크연결

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())

networks = [list(map(int, input().strip().split())) for _ in range(M)]
networks.sort(key= lambda x:x[2])
parent = [i for i in range(N+1)]
ans = 0
for s, e, val in networks:
    if find(s) != find(e):
        union(s, e)
        ans += val

print(ans)