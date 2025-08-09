import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(N)]
max_val = min(N, M)
ans = 1

for i in range(N):
    for j in range(M):
        for k in range(max_val):
            if 0 <= i+k < N and 0 <= j+k < M:
                if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                    ans = max(ans, (k+1)**2)
print(ans)