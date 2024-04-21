import sys
input = sys.stdin.readline

bgs = [int(input()) for _ in range(3)]
drks = [int(input()) for _ in range(2)]

print(min(bgs)+min(drks)-50)