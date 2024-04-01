import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    if num != 0:
        heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)