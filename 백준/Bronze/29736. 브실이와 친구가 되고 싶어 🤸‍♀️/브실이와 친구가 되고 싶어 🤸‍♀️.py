import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
K, X = map(int, input().strip().split())

ans = min(K - A, X) + min(B-K, X) + 1
print(ans if ans > 0 else 'IMPOSSIBLE')