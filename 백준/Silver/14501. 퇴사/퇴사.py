import sys

n = int(sys.stdin.readline())
schedule = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

dp = [0] * (n+1)
for i in range(n):
    for j in range(i+schedule[i][0], n+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
print(dp[-1])
