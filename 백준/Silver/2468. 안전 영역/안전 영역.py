# 안전 영역

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global visited
    visited[x][y] = True
    if x + 1 < n and area[x + 1][y] > limit and not visited[x + 1][y]:
        dfs(x + 1, y)
    if x - 1 >= 0 and area[x - 1][y] > limit and not visited[x - 1][y]:
        dfs(x - 1, y)
    if y + 1 < n and area[x][y + 1] > limit and not visited[x][y + 1]:
        dfs(x, y + 1)
    if y - 1 >= 0 and area[x][y - 1] > limit and not visited[x][y - 1]:
        dfs(x, y - 1)


# n :배열 크기
n = int(sys.stdin.readline())
# 배열
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_cnt = 1
min_h, max_h = 101, 0

# min max값 찾기
for i in range(n):
    for j in range(n):
        if area[i][j] < min_h:
            min_h = area[i][j]
        elif area[i][j] > max_h:
            max_h = area[i][j]

# 높이를 기준으로 배열을 돌면서 dfs를 진행한다.
for limit in range(min_h, max_h + 1):
    # 방문체크용 배열
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > limit and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
