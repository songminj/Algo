# 최소힙

import sys
import heapq
# n : 연산의 개수
n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(heap, num)
    else:
        if heap:
            min_value = heapq.heappop(heap)
            print(min_value)
        else:
            print(0)
