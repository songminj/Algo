# 최대힙

import heapq
import sys
n = int(sys.stdin.readline().strip())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
