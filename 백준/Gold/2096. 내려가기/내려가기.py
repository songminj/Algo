import sys

input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
max_dp = [dp[0][:]] + [[0]*3]
min_dp = [dp[0][:]] + [[0]*3]

for i in range(1, n):
    if i % 2 ==1 :
        max_dp[1][0] = max(max_dp[0][0], max_dp[0][1]) + dp[i][0]
        max_dp[1][1] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + dp[i][1]
        max_dp[1][2] = max(max_dp[0][1], max_dp[0][2]) + dp[i][2]
        min_dp[1][0] = min(min_dp[0][0], min_dp[0][1]) + dp[i][0]
        min_dp[1][1] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + dp[i][1]
        min_dp[1][2] = min(min_dp[0][1], min_dp[0][2]) + dp[i][2]
    else :
        max_dp[0][0] = max(max_dp[1][0], max_dp[1][1]) + dp[i][0]
        max_dp[0][1] = max(max_dp[1][0], max_dp[1][1], max_dp[1][2]) + dp[i][1]
        max_dp[0][2] = max(max_dp[1][1], max_dp[1][2]) + dp[i][2]
        min_dp[0][0] = min(min_dp[1][0], min_dp[1][1]) + dp[i][0]
        min_dp[0][1] = min(min_dp[1][0], min_dp[1][1], min_dp[1][2]) + dp[i][1]
        min_dp[0][2] = min(min_dp[1][1], min_dp[1][2]) + dp[i][2]


if n % 2 == 1:
    print(max(max_dp[0]), min(min_dp[0]))
else:
    print(max(max_dp[1]), min(min_dp[1]))