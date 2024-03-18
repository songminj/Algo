import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
al, bl = len(a), len(b)
dp = [0] * (al)

for w in b:
    cnt = 0
    for idx in range(al):
        if w == a[idx]:
            if cnt < dp[idx]:
                cnt = dp[idx]
            else:
                dp[idx] = cnt +1
        else:
            cnt = max(cnt, dp[idx])
print(max(dp))