import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res = A & B
ic = len(res)
print(a+b-2*ic)