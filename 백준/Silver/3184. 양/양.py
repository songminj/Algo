# 3184번 양

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(R)]

def bfs(x, y):
    global arr
    queue = deque([(x, y)])
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    sheep = 1
    wolf = 0
    arr[x][y] = '#'
    while queue:
        nx, ny = queue.pop()
        for i in range(4):
            dx = nx + delta[i][0]
            dy = ny + delta[i][1]
            if 0 <= dx < R and 0 <= dy < C:
                curr = arr[dx][dy]
                if curr == '#':
                    continue
                elif curr == 'v':
                    wolf += 1
                elif curr == 'o':
                    sheep += 1
                queue.append((dx, dy))
                arr[dx][dy] = '#'
    if sheep > wolf:
        return [True, sheep]
    else:
        return [False, wolf]

s, w = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'o':
            result, cnt = bfs(i, j)
            if result:
                s += cnt
            else:
                w += cnt

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'v':
            w += 1

print(s, w)