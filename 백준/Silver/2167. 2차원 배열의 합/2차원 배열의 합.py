import sys
input = sys.stdin.readline


N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
K = int(input().strip())
for _ in range(K):
    cnt = 0
    i, j, x, y = map(int, input().strip().split())
    for p in range(i-1, x):
        cnt += sum(arr[p][j-1:y])
    print(cnt)