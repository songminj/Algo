import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

cost = []
res = [0] * (N)
def check(lv):
    for i in range(N):
        if cost[i] <= lv:
            return i

for _ in range(N):
    cost.append(int(input().strip()))

for i in range(M):
    lv = int(input())
    res[check(lv)] += 1

print(res.index(max(res))+1)