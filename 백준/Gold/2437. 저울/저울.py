# 2437번 저울

import sys
input = sys.stdin.readline

N = int(input())
chuu = list(map(int, input().strip().split()))
chuu.sort()

min_val = 1
for c in chuu:
    if c > min_val:
        break
    min_val += c

print(min_val)