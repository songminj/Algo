import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
T = [int(input()) for _ in range(N)]

def binary(s, e):
    while s <= e:
        mid = (s + e) // 2
        checked = 0
        for t in T:
            checked += (mid // t)
        if checked >= M:
            e = mid - 1
        else:
            s = mid + 1
    return s

print(binary(1, max(T) * M))