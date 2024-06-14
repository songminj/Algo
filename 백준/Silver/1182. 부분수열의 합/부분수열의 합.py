# 1182번 부분수열의 합

import sys
input = sys.stdin.readline

n, s = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

cnt = 0
for m in range(1, 1 << n):
    subset_sum = 0
    for i in range(n):
        if m & (1 << i):
            subset_sum += arr[i]
    if subset_sum == s:
        cnt += 1
print(cnt)