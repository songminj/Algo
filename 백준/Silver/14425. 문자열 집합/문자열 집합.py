import sys
input = sys.stdin.readline

N, M = map(int, input().split())
checks = set(input().strip() for _ in range(N))
cnt = 0
for i in range(M):
    target = set([input().strip()])
    if not target - checks:
        cnt += 1
print(cnt)