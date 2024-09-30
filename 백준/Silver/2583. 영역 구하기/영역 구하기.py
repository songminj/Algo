# 2584 영역구하기

import sys
from collections import deque
input = sys.stdin.readline

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(x, y):
    queue = deque([(x, y)])
    cnt = 1
    board[x][y] = 1
    while queue:
        p, q = queue.popleft()
        for i in range(4):
            dx = p + delta[i][0]
            dy = q + delta[i][1]
            if 0 <= dx < M and 0 <= dy < N:
                if board[dx][dy] == 0:
                     queue.append((dx, dy))
                     cnt += 1
                     board[dx][dy] = 1
    return cnt

M, N, K = map(int, input().strip().split())
board = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for i in range(y1, y2):
        board[i][x1:x2] = [1]*(x2-x1)

res = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            res.append(bfs(i, j))
res.sort()
print(len(res))
print(*res)