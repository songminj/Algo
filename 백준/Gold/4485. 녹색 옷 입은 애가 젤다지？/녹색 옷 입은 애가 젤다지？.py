# 4485 녹색 옷 입은 애가 젤다지?

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dijkstra(id, n, arr):
    pq = []
    dist = [[1e9] * n for _ in range(n)]
    dist[0][0] = arr[0][0]
    heappush(pq, (dist[0][0], 0, 0))
    while pq:
        d, x, y = heappop(pq)
        if x == n-1 and y == n-1:
            print(f'Problem {id}: {d}')
            return
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            if 0 <= dx < n and 0 <= dy < n:
                cost = d + arr[dx][dy]
                if dist[dx][dy] > cost:
                    dist[dx][dy] = cost
                    heappush(pq, (cost, dx, dy))
    return

id = 0
while True:
    N = int(input())
    if N == 0:
        break
    id += 1
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    dijkstra(id, N, arr)
