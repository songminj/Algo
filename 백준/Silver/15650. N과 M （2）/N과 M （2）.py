import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

def nm(val, cnt, idx):
    if cnt == M:
        print(*val)
        return
    for i in range(idx, N+1):
        if i not in val:
            nxt = val + [i]
            nm(nxt, cnt +1, i)

nm([], 0, 1)