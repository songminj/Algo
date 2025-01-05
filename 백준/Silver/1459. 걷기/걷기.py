import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().strip().split())

straight = (x + y) * w

if (x + y) % 2 == 0:
    diagonal = max(x, y) * s
else:
    diagonal = (max(x, y) - 1) * s + w

mixed = min(x, y) * s + abs(x - y) * w

print(min(straight, diagonal, mixed))