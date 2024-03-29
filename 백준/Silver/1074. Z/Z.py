import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())
ans = 0
while N:
    N -= 1
    slice = 2 ** N
    # 2사분면
    if r < slice and c >= slice:
        ans += slice * slice * 1
        c -= slice
    # 1사분면
    elif r < slice and c < slice:
        ans += slice * slice * 0
    # 3사분면
    elif r >= slice and c < slice:
        ans += slice * slice * 2
        r -= slice
    # 4사분면
    else:
        ans += slice * slice * 3
        r -= slice
        c -= slice

print(ans)
