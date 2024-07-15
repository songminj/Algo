# 15961번 회전 초밥

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().strip().split())
belt = list(int(input()) for _ in range(N))

sushi = {}
max
# 처음 k개
for i in range(k):
    sushi[belt[i]] = sushi.get(belt[i], 0) + 1
# 쿠폰
sushi[c] = sushi.get(c, 0) +1

cur_v = len(sushi.keys())
max_v = cur_v
for i in range(N):
    e = belt[(k+i)%N]
    sushi[e] = sushi.get(e, 0) + 1
    s = belt[i]
    sushi[s] -= 1
    if sushi[s] == 0:
        sushi.pop(s)
    max_v = max(max_v, len(sushi.keys()))
print(max_v)