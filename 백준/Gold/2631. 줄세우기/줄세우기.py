# 2631번 줄세우기

import sys
input = sys.stdin.readline

N = int(input())
child = [int(input()) for _ in range(N)]
dp = [1] * N

for i in range(N):
    for j in range(i):
        if child[i] > child[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(N-max(dp))