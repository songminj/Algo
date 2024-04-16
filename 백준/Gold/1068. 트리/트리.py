import sys
input = sys.stdin.readline

from collections import deque
N = int(input())

parents = list(map(int, input().split()))


leaf = [1] * N

rm = int(input())
def remove_node(rm):
    roots = deque([(rm)])
    leaf[rm] = 0
    while roots:
        r = roots.popleft()
        for i in range(N):
            if parents[i] == r:
                roots.append(i)
                leaf[i] = 0
remove_node(rm)

for i in range(N):
    if i != rm and parents[i] != -1:
        leaf[parents[i]] = 0
print(leaf.count(1))