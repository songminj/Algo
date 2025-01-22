# 14490번 백대열

import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, input().strip().split(':'))
t = gcd(a, b)
print(int(a/t),':',int(b/t), sep='')