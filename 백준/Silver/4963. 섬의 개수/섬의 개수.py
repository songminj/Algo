import sys
input = sys.stdin.readline
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
def bfs(i, j):
    global visited
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            dx = x + delta[k][0]
            dy = y + delta[k][1]
            if 0 <= dx < h and 0 <= dy < w:
                if arr[dx][dy] == '1' and not visited[dx][dy]:
                    visited[dx][dy] = True
                    queue.append((dx, dy))

while True:
    w, h = map(int, input().split())
    if (w+h) == 0:
        break
    arr = [list(input().split()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == '1':
                bfs(i, j)
                cnt += 1
    print(cnt)