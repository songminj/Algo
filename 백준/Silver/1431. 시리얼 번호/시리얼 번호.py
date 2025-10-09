# 1431 시리얼 번호

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
len_graph = {i : [] for i in range(1, 51)}
for _ in range(N):
    x = input().strip()
    len_graph[len(x)].append(x)

def filter(lst: list):
    pq = []
    for num in lst:
        cnt = 0
        for n in num:
            if n in '0123456789':
               cnt += int(n)
        heappush(pq, (cnt, num))
    return [heappop(pq)[1] for _ in range(len(lst))]

for i in range(1, 51):
    if len_graph[i]:
        tg = filter(len_graph[i])
        print(*tg, sep='\n')