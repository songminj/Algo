import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
cars = list(map(int, input().split()))

for c in cars:
    if c == N:
        cnt += 1

print(cnt)