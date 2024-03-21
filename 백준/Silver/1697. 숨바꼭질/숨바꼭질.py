import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for next in (x-1, x+1, 2*x):
            if 0 <= next < 100001 and not visited[next]:
                visited[next] = visited[x] +1
                queue.append(next)

visited = [0] * 100001
print(bfs(n))
