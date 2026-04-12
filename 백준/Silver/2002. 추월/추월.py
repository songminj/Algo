# 2002번 추월

import sys
input = sys.stdin.readline

N = int(input())
entry = {input().strip() : i for i in range(N)}
exit = list(int(entry[input().strip()]) for _ in range(N))

res = 0
for i in range(N):
    for j in range(i, N):
        if exit[i] > exit[j]:
            res += 1
            break

print(res)