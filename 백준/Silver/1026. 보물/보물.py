import sys


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

a_sort = sorted(a)
b_sort = sorted(b.copy(), reverse=True)

res = 0
for i in range(n):
    res += a_sort[i]*b_sort[i]
print(res)

