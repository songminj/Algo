# 1253 좋다

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))
nums.sort()
res = 0

for i in range(N):
    target = nums[i]
    l, r = 0, N-1

    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        now = nums[l]+nums[r]

        if now == target:
            res += 1
            break
        elif now < target:
            l += 1
        else:
            r -= 1

print(res)