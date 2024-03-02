import sys

n = int(sys.stdin.readline())
nums = sys.stdin.readline().strip().split()
dp = [[1, 1] for _ in range(n)]

max_dp = 1
for i in range(1, n):
    if nums[i] >= nums[i - 1]:
        dp[i][0] += dp[i - 1][0]
        if max_dp < dp[i][0]:
            max_dp = dp[i][0]

    if nums[i] <= nums[i - 1]:
        dp[i][1] += dp[i - 1][1]
        if max_dp < dp[i][1]:
            max_dp = dp[i][1]
# print(dp)
print(max_dp)