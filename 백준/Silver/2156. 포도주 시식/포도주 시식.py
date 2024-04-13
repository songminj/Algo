import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * n
wines = [int(input()) for _ in range(n)]

dp[0] = wines[0]
if n < 3:
    print(sum(wines))
else:
    dp[1] = dp[0]+wines[1]
    dp[2] = max(wines[2] + dp[0], wines[2]+wines[1], dp[1])
    if n > 3:
        for i in range(3, n):
            dp[i] = max(wines[i] + wines[i-1] + dp[i-3], wines[i] + dp[i-2], dp[i-1])
    print(dp[-1])