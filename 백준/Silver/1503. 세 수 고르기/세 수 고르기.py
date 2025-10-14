# 1503번 세 수 고르기

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
s = list(map(int, input().rstrip().split()))
res = float("inf")

for i in range(1, 1002):
    if i in s: continue
    for j in range(1, 1002):
        if j in s: continue
        for k in range(1, 1002):
            if k in s: continue
            q = (i * j * k)
            if abs(N - q) < res: res = abs(N - q)
            if N + 1 < q: break
print(res)