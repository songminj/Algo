import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

for i in range(n):
    if tree[i] <= m:
        m += 1
    else:
        break
print(m)