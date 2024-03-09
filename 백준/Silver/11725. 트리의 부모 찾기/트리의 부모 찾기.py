import sys
sys.setrecursionlimit(10**8)

n = int(sys.stdin.readline())
adj_dic = {i : [] for i in range(1, n+1)}

def dfs(num):
    for w in adj_dic[num]:
        if not visited[w]:
            visited[w] = num
            dfs(w)

for _ in range(n-1):
    start, end = map(int, sys.stdin.readline().strip().split())
    adj_dic[start] += [end]
    adj_dic[end] += [start]

visited = [False for _ in range(n+1)]
dfs(1)
for i in range(2, n+1):
    print(visited[i])
