import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
basket = ['0'] * (N + 1)
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        basket[x] = str(k)

print(' '.join(basket[1:]))