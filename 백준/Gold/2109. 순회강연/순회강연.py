# 2109번 순회강연

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

info = [list(map(int, input().strip().split())) for _ in range(n)]
info.sort(key=lambda x : x[1])
pq = []
for pay, day in info:
    heappush(pq, pay)
    if day < len(pq):
        heappop(pq)

print(sum(pq))