# 1449 수리공 항승

import sys
input = sys.stdin.readline

N, L = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()
idx = 0
ans = 0
for a in arr:
    if a < idx:
        continue
    idx = a + L
    ans += 1
print(ans)