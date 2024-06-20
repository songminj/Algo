# 1351번 무한 수열
# idea : DP문제,, 수학문제?

import sys
from collections import defaultdict
input = sys.stdin.readline

N, P, Q = map(int, input().split())
nums = defaultdict(int)
nums[0] = 1

def fib(n):
    if nums[n] !=0:
        return nums[n]
    nums[n] = fib(n//P) + fib(n//Q)
    return nums[n]
print(fib(N))