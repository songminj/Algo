def dfs(start):
    global visited
    visited[start] = True
    stack = [start]

    while stack:
        next = stack.pop()
        for w in adj_dic[next]:
            if visited[w] == False:
                visited[w] = True
                stack.append(w)


test_case = int(input())
for T in range(1, test_case + 1):
    n, m = map(int, input().split())
    # 인접행렬
    adj_dic = {i: [] for i in range(1, n + 1)}
    visited = [False for _ in range(n + 1)]
    cnt = 0
    for _ in range(m):
        start, end = map(int, input().split())
        adj_dic[start].append(end)
        adj_dic[end].append(start)

    # 무리 개수 세기
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(f'#{T} {cnt}')