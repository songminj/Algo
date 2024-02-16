
from collections import deque

def bfs(v, n): # v : 시작 정점, 노드개수 : n
    q = deque()  # 큐
    visited = [0] * (n+1)    # visited
    q.append(v)    # 시작점 인큐
    visited[v] = 1    # 시작점 방문표시
    while q:
        t = q.popleft()
        # print(t)
        result_bfs.append(t)
        for i in adj_list[t]:   # t에 인접한 정점 i
            if visited[i] == 0:     # 방문하지 않은 정점이면
                q.append(i)
                visited[i] = 1 + visited[t] # 방문표시, 거리정보?


# 재귀 dfs
def dfs(v):
    visited_dfs[v] = 1
    result_dfs.append(v)

    for w in adj_list[v]:
        if visited_dfs[w] == 0:
            dfs(w)


# 데이터 받기
n, m, v = map(int, input().split())

# 인접행렬만들기
adj_list = [[] for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    adj_list[start] += [end]
    adj_list[end] += [start]
# 인접행렬 정렬
for i in range(n+1):
    adj_list[i] = sorted(adj_list[i])

# print(adj_list)

# 필요한거
queue = deque()
stack = []
result_bfs = []
result_dfs = []
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

# 함수 호출
bfs(v, n)
dfs(v)
print(*result_dfs)
print(*result_bfs)
