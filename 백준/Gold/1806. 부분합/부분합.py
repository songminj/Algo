# 1806 부분합

import sys
input = sys.stdin.readline

N, S = map(int,input().strip().split())
arr = list(map(int, input().strip().split()))
l, r = 0, 0
ans = 100001
sum_val = 0

while True:
    if sum_val >= S:
        ans = min(ans, r - l)
        sum_val -= arr[l]
        l += 1
    elif r == N:
        break
    else:
        sum_val += arr[r]
        r += 1

print(0 if ans == 100001 else ans)