
paper = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 3
if paper > 2:
    for i in range(3, paper + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[paper]%10007)