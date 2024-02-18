num = int(input())

stair = [0] * (301)
for i in range(1, num+1):
    stair[i] = int(input())

dp = [0, stair[1], stair[1] + stair[2], max(stair[1] + stair[3], stair[2] + stair[3])]
if num > 3:
    dp.extend([0]*(num-3))
    for i in range(4, num+1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[num])