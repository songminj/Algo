# 2457번 공주님의 정원

import sys
input = sys.stdin.readline

N = int(input())
flowers = []

for _ in range(N):
    m1, d1, m2, d2 = map(int, input().strip().split())
    flowers.append((m1*100 + d1, m2*100 + d2))

flowers.sort()
start, end = 301, 301
count = 0
idx = 0

while end <= 1130:
    max_end = end

    while idx < N and flowers[idx][0] <= end:
        max_end = max(max_end, flowers[idx][1])
        idx += 1
    if max_end == end:
        print(0)
        exit()
    end = max_end
    count += 1

print(count)