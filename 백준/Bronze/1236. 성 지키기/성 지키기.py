import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

r, c =[], []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'X':
            break
    else:
        c.append(i)

for j in range(M):
    for i in range(N):
        if arr[i][j] == 'X':
            break
    else:
        r.append(j)
print(max(len(r), len(c)))