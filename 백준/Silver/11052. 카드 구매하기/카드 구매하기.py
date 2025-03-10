# 11052번 카드 구매하기

import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().strip().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], nums[j]+dp[i-j])
print(dp[-1])