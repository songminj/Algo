import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    cnt = 0
    for _ in range(N):
        v, f, c = map(int, input().split())
        max_len = v * (f // c) + v * ((f % c) / c)
        if D <= max_len:
            cnt += 1

    print(cnt)