# 11652번 카드

import sys
input = sys.stdin.readline

N = int(input())
cnt = dict()
ans = []

for _ in range(N):
    num = int(input())
    cnt[num] = cnt.get(num, 0) + 1

for key, value in cnt.items():
    ans.append((key, value))
ans.sort(key = lambda x : (-x[1], x[0]))

print(ans[0][0])