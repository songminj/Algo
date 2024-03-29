import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = [1] * N

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))