# 11660번 구간합 구하기 5

import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
if m != 0:
    nums = input().strip().split()

ans = 0

def testing(target):
    for c in nums:
        if c in target:
            continue
        else:
            return 0
    else:
        return 1

if m == 0:
    print(10**n)
else:
    for i in range(1, 10**n):
        testnum = str(i).zfill(n)
        ans += testing(testnum)
    print(ans)