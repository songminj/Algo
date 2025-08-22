# 17070번 파이프 옮기기 1

import sys
input = sys.stdin.readline

inf = 1e9
N, M = map(int, input().strip().split())
dp = [inf] * 7

for i in range(M):
    pkg, one = map(int, input().strip().split())
    for j in range(1, 6):
        dp[j] = min(one * j, dp[j])
    dp[6] = min(pkg, dp[6], one*6)

div, mod = N // 6, N % 6
if mod == 0:
    print(dp[6] * div)
else:
    print(min(dp[6] * (div + 1), dp[mod] + dp[6] * div))
