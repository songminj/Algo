import sys
sys.setrecursionlimit(10**8)

n, root, q = map(int, sys.stdin.readline().strip().split())
tree = {i: [] for i in range(1, n + 1)}
count = [0] * (n+1)
for i in range(n - 1):
    s, e = map(int, sys.stdin.readline().strip().split())
    tree[s] += [e]
    tree[e] += [s]

def count_trees(x):
    count[x] = 1
    for i in tree[x]:
        if not count[i]:
            count_trees(i)
            count[x] += count[i]

count_trees(root)

for _ in range(q):
    start = int(sys.stdin.readline().strip())
    print(count[start])
