import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]+[0] * (N-1)

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])
        else:
            dp[i] = max(dp[i], arr[i])
print(max(dp))