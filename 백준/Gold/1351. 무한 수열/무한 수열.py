# 1351번 무한 수열
# 자료구조와 dp를 적절히 섞어서 

import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())
nums = {0:1}

def fib(n):
    if n in nums:
        return nums[n]
    nums[n] = fib(n//P) + fib(n//Q)
    return nums[n]
print(fib(N))
