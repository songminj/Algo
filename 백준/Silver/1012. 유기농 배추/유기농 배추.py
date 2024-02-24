# 유기농배추
import sys

def dfs(graph):
    global cnt
    stack = []
    for spot in graph.keys():
        if visited[spot] == 0:
            cnt += 1
            # print(spot)
            visited[spot] == 1
            stack.append(spot)
            while stack:
                step = stack.pop()
                if visited[step] == 0:
                    visited[step] = 1
                    stack.extend(graph[step])


test_case = int(sys.stdin.readline())
for i in range(test_case):
    # m:가로길이 n: 세로길이, k : 배추
    m, n, k = map(int, sys.stdin.readline().split())
    farm = [[0] * n for _ in range(m)]
    adj_dic = {}
    visited = {}
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        adj_dic.setdefault((x, y), [])
        visited.setdefault((x, y), 0)
    # print('visit', visited)
    for a, b in adj_dic:
        # print(a, b)
        for i in range(4):
            ni = a + di[i]
            nj = b + dj[i]
            if (ni, nj) in adj_dic.keys(): # and 0 <= ni <= n and 0 <= nj < m:
                adj_dic[(a, b)] += [(ni, nj)]
                adj_dic[(ni, nj)] += [(a, b)]
    # print('adj', adj_dic)
    cnt = 0
    dfs(adj_dic)
    print(cnt)