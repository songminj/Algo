# 14495번 피보나치 비스무리한 수열

N = int(input())

def fib(n):
    dp = [1] * (n+1)
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3]
    return dp[n]

if N <= 3:
    print(1)
else:
    print(fib(N))