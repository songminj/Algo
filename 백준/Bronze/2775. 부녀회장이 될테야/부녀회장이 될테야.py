import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    K, N = int(input()), int(input())
    # 0층 dp
    dp = [i for i in range(15)]
    for _ in range(K):
        for i in range(1, N+1):
            dp[i] += dp[i-1]
    print(dp[N])