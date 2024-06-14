# 2225번 합분해

n, k = map(int, input().strip().split())
dp = [[1] * (n+1) for _ in range(k)]

for i in range(1, k):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1] % int(1e9))