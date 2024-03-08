import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)
dp[1] = [0] + list(map(int, sys.stdin.readline().strip().split())) + [0]
for i in range(2, n+1):
    dp[i] = [0] + list(map(int, sys.stdin.readline().strip().split())) + [0]
    for j in range(1, i+1):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n]))
