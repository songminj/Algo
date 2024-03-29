import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
updp = [1] * N
downdp = [1] * N

for i in range(1, N):
    for j in range(i):
        if seq[i] > seq[j]:
            updp[i] = max(updp[i], updp[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if seq[i] > seq[j]:
            downdp[i] = max(downdp[i], downdp[j] + 1)
res = 0
for i in range(N):
    if res < (updp[i] + downdp[i] - 1):
        res = updp[i] + downdp[i] - 1
print(res)
