import sys

input = sys.stdin.readline

N = int(input())
visited = [False] * (N+1)
def perm(lst):
    if len(lst) == N:
        print(*lst)
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            perm(lst+[i])
            visited[i] = False

perm([])
