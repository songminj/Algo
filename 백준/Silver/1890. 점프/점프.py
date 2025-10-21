# 1890번 점프

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
  for j in range(N):
    x = arr[i][j]
    if x == 0 or dp[i][j] == 0:
      continue
    if x + i < N:
      dp[i+x][j] += dp[i][j]
    if x + j < N:
      dp[i][j+x] += dp[i][j]
print(dp[-1][-1])