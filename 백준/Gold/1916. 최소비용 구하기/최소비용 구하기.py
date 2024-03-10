import sys
import heapq

# n : 도시개수
n = int(sys.stdin.readline())
INF = 1e8
def dijk(adj_dic, start, end):
    d = {i : INF for i in range(1, n+1)}
    d[start] = 0
    queue = []
    heapq.heappush(queue, [d[start], start])    # 시작노드부터 탐색을 시작할것임

    while queue:
        now_d, now_node = heapq.heappop(queue)
        if d[now_node] < now_d:
            continue
        for new_node, new_d in adj_dic[now_node]:
            distance = now_d + new_d
            if distance < d[new_node]:
                d[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
    return d[end]

# m : 버스 개수
m = int(sys.stdin.readline())
adj_dic = {i : [] for i in range(1, n+1)}

# 출발 : {도착:비용} 형태로 만들기
for _ in range(m):
    s, e, d = map(int, sys.stdin.readline().strip().split())
    adj_dic[s].append([e, d])
# print(adj_dic)
start, end = map(int, sys.stdin.readline().strip().split())

print(dijk(adj_dic, start, end))