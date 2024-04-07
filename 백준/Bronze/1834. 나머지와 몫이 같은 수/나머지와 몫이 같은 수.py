import sys
input = sys.stdin.readline

res = 0
N = int(input())
for i in range(1, N):
    res += (i + i*N)
print(res)