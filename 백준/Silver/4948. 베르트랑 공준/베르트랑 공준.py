import sys
input = sys.stdin.readline

m = 123457*2
prime = [True for _ in range(m+1)]
prime[1] = False
msqrt = int(m**0.5)
for i in range(2, msqrt+1):
    if prime[i] == True:
        for j in range(i+i, m, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if prime[i]:
            cnt += 1
    print(cnt)