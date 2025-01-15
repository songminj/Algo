import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().strip().split())
    if (a >= b) :
        print("MMM BRAINS")
    else:
        print("NO BRAINS")