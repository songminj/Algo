import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()

def nm(val, cnt, idx):
    if cnt == M:
        print(*val)
        return
    for i in range(idx, N):
        if arr[i] not in val:
            nxt = val + [arr[i]]
            nm(nxt, cnt +1, i+1)

nm([], 0, 0)