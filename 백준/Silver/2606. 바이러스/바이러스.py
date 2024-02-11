import sys
# pc : node e: edge
pc = int(sys.stdin.readline())
e = int(sys.stdin.readline())
adj_list = [[] for _ in range(pc+1)]

virus = []
def dfs(start):
    visited[start] = 1
    virus.append(start)

    for w in adj_list[start]:
        if visited[w] == 0:
            dfs(w)


for i in range(e):
    start, end = map(int, sys.stdin.readline().split())
    adj_list[start] += [end]
    adj_list[end] += [start]

visited = [0] * (pc+1)
dfs(1)
print(len(virus)-1)