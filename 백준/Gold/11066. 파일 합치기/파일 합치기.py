# 11066번 파일합치기

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().strip().split()))
    prefix = [0] * (K+1)
    for i in range(1, K+1):
        prefix[i] = prefix[i-1] + files[i]
    dp = list([0] * (K+1) for _ in range(K+1))
    for i in range(1, K):
        for s in range(1, K-i+1):
            e = s+i
            min_val = sys.maxsize
            for mid in range(s, e):
                min_val = min(min_val, dp[s][mid] + dp[mid+1][e])

            dp[s][e] = min_val + prefix[e] - prefix[s-1]
    print(dp[1][K])