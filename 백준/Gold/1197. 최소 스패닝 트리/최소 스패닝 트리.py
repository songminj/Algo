# 1197번 최소 스패닝 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().strip().split())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [ i  for i in range(V+1)]
answer = 0
tree = [list(map(int, input().strip().split())) for _ in range(E)]
tree.sort(key = lambda x : x[2])

for s, e, val in tree:
    if find(s) != find(e):
        union(s, e)
        answer += val

print(answer)