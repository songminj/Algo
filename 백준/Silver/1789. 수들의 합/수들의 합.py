import sys

n = int(sys.stdin.readline())
a = int((2*n)**(1/2))
for i in range(a, 0, -1):
    if i * (i+1) <= 2*n:
        print(i)
        break