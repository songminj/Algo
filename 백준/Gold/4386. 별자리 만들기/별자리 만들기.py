# 4386번 별자리 만들기

import sys
import math
input = sys.stdin.readline


N = int(input())
stars = [tuple(map(float, input().strip().split())) for _ in range(N)]
edges = []
parent = list(range(N))

for i in range(N):
    for j in range(i+1, N):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        dist = math.sqrt((x1- x2)** 2 + (y1-y2)**2)
        edges.append((dist, i, j))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

edges.sort()
mst_cost =0
for cost, a, b in edges:
    if union(a, b):
        mst_cost += cost

print(f"{mst_cost:.2f}")