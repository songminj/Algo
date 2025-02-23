# 1769번 3의 배수

import sys
input = sys.stdin.readline
X = input().strip()
count = 0

while len(X) != 1:
    cnt = 0
    for n in X:
        cnt += int(n)
    X = str(cnt)
    count += 1
print(count)
print('YES'if int(X) % 3 == 0  else'NO')