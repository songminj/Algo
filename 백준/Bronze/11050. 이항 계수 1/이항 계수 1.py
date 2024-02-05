# 자연수 N과 정수 K
N, K = map(int, input().split())

son = 1
for i in range(N, 0, -1): 
    son *= i
mom1 = 1
for i in range(N-K, 0, -1):
    mom1 *= i
mom2 = 1
for i in range(K, 0, -1):
    mom2 *= i

if 0<= K <= N :
    result = int(son / (mom1*mom2))
elif K < 0 or K > N :
    result = 0

print(result)