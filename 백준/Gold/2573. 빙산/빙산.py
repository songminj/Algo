import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(n)]

def bfs(p, q):
    global visited
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    queue.append((p, q))
    visited[p][q] = True
    melt_list = []

    while queue:
        a, b = queue.popleft()
        ice = 0
        for k in range(4):
            di = a + delta[k][0]
            dj = b + delta[k][1]
            if arr[di][dj] == 0:
                ice += 1
            if arr[di][dj] > 0 and not visited[di][dj]:
                visited[di][dj] = True
                queue.append((di, dj))
        if arr[a][b] > 0:
            melt_list.append((a, b, ice))

    for a, b, ice in melt_list:
        arr[a][b] -= ice
        if arr[a][b] < 0:
            arr[a][b] = 0

round = 0
while True:
    round += 1
    res = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                res += 1

    if res == 0:
        print(0)
        break
    elif res > 1:
        print(round - 1)
        break
