import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque([i for i in range(1, N + 1)])
cnt = 1
res = []
while queue:
    if cnt % K == 0:
        tmp = queue.popleft()
        res.append(str(tmp))
    else:
        queue.rotate(-1)
    cnt += 1
print('<', end='')
print(', '.join(res), end='')
print('>')