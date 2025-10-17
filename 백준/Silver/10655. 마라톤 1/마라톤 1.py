# 10655번 마라톤 1

import sys
input = sys.stdin.readline

N = int(input())
ans = [0] * N
cp = [list(map(int, input().split())) for _ in range(N)]

def distance(a, b):
    return abs(cp[a][0] - cp[b][0]) + abs(cp[a][1] - cp[b][1])

max_diff = -float('inf')
result = 0
for i in range(N-1) :
  d = distance(i, i+1)
  result += d
  if i < N-2 :
    dist2 = distance(i+1, i+2)
    next_dist = distance(i, i+2)
    max_diff = max(max_diff, d + dist2 - next_dist)

print(result - max_diff)