# 11653번 소인수분해

N = int(input())
n = int(N**(1/2))

for i in range(2, max(n+1, N+1)):
    while N % i == 0:
        N = N // i
        print(i)