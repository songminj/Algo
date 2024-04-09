import sys
input = sys.stdin.readline

fx = input().strip().split('-')

# 더하기 먼저 계산
for i in range(len(fx)):
    tmp = fx[i].split('+')
    cnt = 0
    for j in range(len(tmp)):
        cnt += int(tmp[j])
    fx[i] = cnt

res = fx[0]
# 빼기 계산
for i in range(1 , len(fx)):
    res -= fx[i]
print(res)