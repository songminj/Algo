# 17070번 파이프 옮기기 1

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[[0]* 3 for _ in range(N)] for _ in range(N)]
# 0 : 끝이 가로 / 1: 끝이 세로 / 2: 끝이 대각선
dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if arr[i][j] == 1:
            continue
        # 가로
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        # 세로
        if i > 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        # 대각선
        if i > 0 and arr[i - 1][j] == 0 and arr[i][j - 1] == 0:
            dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

print(sum(dp[-1][-1]))