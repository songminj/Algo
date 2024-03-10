import sys
import heapq

InF = float('inf')

def dijk(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])
    while queue:
        now_d, now_node = heapq.heappop(queue)
        if distance[now_node] < now_d:
            continue
        for new_node, new_d in adj_dic[now_node]:
            d = now_d + new_d
            if d < distance[new_node]:
                distance[new_node] = d
                heapq.heappush(queue, [d, new_node])

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
adj_dic = {i : [] for i in range(1, v+1)}
for _ in range(e):
    s, e, w = map(int, sys.stdin.readline().strip().split())
    adj_dic[s].append([e, w])

distance = { i : InF for i in range(1, v+1)}
dijk(k)
for j in range(1, v+1):
    if distance[j] == float('inf'):
        print('INF')
    else:
        print(distance[j])
