import sys
input = sys.stdin.readline

tc = int(input())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(tc):
    a, b = map(int, input().strip().split())
    newa, newb = max(a, b), min(a, b)
    print(gcd(newa,newb))