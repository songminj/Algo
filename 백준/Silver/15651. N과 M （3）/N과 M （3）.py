import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def nm(val, cnt):
    if cnt == M:
        print(*val)
        return
    for i in range(1, N+1):
        nxt = val + [i]
        nm(nxt, cnt +1)

nm([], 0)