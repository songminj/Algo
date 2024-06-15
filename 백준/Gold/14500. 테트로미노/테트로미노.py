# 14500번 테트로미노
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for _ in range(n)]

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
res = 0

def dfs(x, y, k, cnt):
	global res, visited
	if k == 3:
		if res < cnt:
			res = cnt
		return

	for i in range(4):
		dx = x + delta[i][0]
		dy = y + delta[i][1]
		if k == 1:
			kx = x + delta[(i + 1) % 4][0]
			ky = y + delta[(i + 1) % 4][1]
			if 0 <= dx < n and 0 <= dy < m and 0 <= kx < n and 0 <= ky < m:
				if not visited[dx][dy] and not visited[kx][ky]:
					visited[dx][dy] = True
					visited[kx][ky] = True
					dfs(dx, dy, k + 2, cnt + board[dx][dy] + board[kx][ky])
					visited[dx][dy] = False
					visited[kx][ky] = False
		if 0 <= dx < n and 0 <= dy < m:
			if not visited[dx][dy]:
				visited[dx][dy] = True
				dfs(dx, dy, k+1, cnt+board[dx][dy])
				visited[dx][dy] = False

visited = [[False] * m for _ in range(n)]
for i in range(n):
	for j in range(m):
		visited[i][j] = True
		dfs(i, j, 0, board[i][j])
		visited[i][j] = False
print(res)