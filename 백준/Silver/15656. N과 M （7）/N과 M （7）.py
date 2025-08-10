import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()

def nm(val, cnt):
    if cnt == M:
        print(' '.join(val))
        return
    for i in range(N):
        nxt = val + [str(arr[i])]
        nm(nxt, cnt +1)

nm([], 0)