# 1757번 달려달려

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

stress = [0] + [int(input().strip()) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = dp[i-1][0]
    for j in range(1, M+1):
        # 달린다
        dp[i][j] = dp[i-1][j-1] + stress[i]
        # 안달린다
        dp[i][0] = max(dp[i][0], dp[i-j][j])
print(dp[-1][0])