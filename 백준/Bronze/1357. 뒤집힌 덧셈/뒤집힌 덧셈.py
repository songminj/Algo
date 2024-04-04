import sys

input = sys.stdin.readline

X, Y = map(int, input().split())

def rev(num):
    res = ''
    while num > 0:
        n = num % 10
        res += str(n)
        num = num // 10
    return int(res)
print(rev(rev(X)+rev(Y)))