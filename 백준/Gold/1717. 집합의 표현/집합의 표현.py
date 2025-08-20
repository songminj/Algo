import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().strip().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def hap(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def is_contain(a, b):
    return find(a) == find(b)

for _ in range(m):
    f, a, b = map(int, input().strip().split())
    if f == 0:
        hap(a, b)
    else:
        print('YES' if is_contain(a, b) else 'NO')