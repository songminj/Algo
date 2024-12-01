import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
l_heap = []
r_heap = []

for _ in range(N):
    n = int(input())
    if len(l_heap) == len(r_heap):
        heappush(l_heap, (-n, n))
    else:
        heappush(r_heap, (n, n))

    if r_heap and l_heap[0][1] > r_heap[0][0]:
        min_val = heappop(r_heap)[0]
        max_val = heappop(l_heap)[1]
        heappush(l_heap, (-min_val, min_val))
        heappush(r_heap, (max_val, max_val))
    print(l_heap[0][1])
