# 22233번 가희와 키워드

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
gahee = set()

for _ in range(N):
    gahee.add(input().strip())

for _ in range(M):
    memo = set(input().strip().split(","))
    gahee -=memo
    print(len(gahee))