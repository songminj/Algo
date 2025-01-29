# 15702번 중간고사 채점

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
values = list(map(int, input().strip().split()))
res = [-1, -1]
for _ in range(M):
    num, *records = input().strip().split()
    score = 0
    num = int(num)
    for i in range(N):
        if records[i] == 'O':
            score += values[i]
    if res[1] < score or (res[1] == score and res[0] > num):
        res = [num, score]

print(*res)