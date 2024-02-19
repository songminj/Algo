test_case = int(input())

dp = [0, 1, 1, 1]
for _ in range(test_case):
    num = int(input())
    dp += [0]*(num)     # 그냥 넉넉하게
    if num > 3:
        for i in range(4, num+1):
            dp[i] = dp[i-3] + dp[i-2]
    print(dp[num])