# 2252번 줄 세우기

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
# 진입차수를 0으로 초기화

indegree = [0] * (N+1)
students = { i : [] for i in range(1, N+1)}

def make_row():
    queue = deque([])
    res = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        x = queue.popleft()
        res.append(str(x))
        for i in students[x]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    print(' '.join(res))


for _ in range(M):
    a, b = map(int, input().strip().split())
    students[a].append(b)
    indegree[b] += 1

make_row()