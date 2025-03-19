# 1715번 카드 정렬하기

import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
heapify(arr)

ans = 0
while len(arr) > 1:
    a = heappop(arr)
    b = heappop(arr)
    sum_val = a+b

    ans += sum_val
    heappush(arr, sum_val)

print(ans)