import sys

input = sys.stdin.readline

def roundcal(x):
    if (x - int(x)) >= 0.5:
        return int(x)+1
    else:
        return int(x)
n = int(input())
levels = sorted([int(input()) for _ in range(n)])
nono = roundcal(n*0.15)

total = sum(levels[nono:n-nono])
people = n - (2*nono)
if people:
    print(roundcal(total/people))
else:
    print(0)