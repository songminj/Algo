# 10867번 중복 빼고 정렬하기

import sys
input = sys.stdin.readline
from heapq import heapify, heappop

N = int(input())
nums = list(map(int, input().strip().split()))
heapify(nums)

last = -1001

while nums:
    x = heappop(nums)
    if last != x:
        print(x, end=' ')
        last = x