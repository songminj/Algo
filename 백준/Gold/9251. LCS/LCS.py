import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
al, bl = len(a), len(b)
dp = [[0] * (bl+1) for _ in range(al+1)]

for i in range(1, al+1):
    for j in range(1, bl+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])